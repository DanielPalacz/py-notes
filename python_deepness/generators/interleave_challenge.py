from typing import Iterable
from typing import Iterator


def interleave(*iterables):
    for zit in zip(*iterables):
        zit_n = len(zit)
        for i in range(zit_n):
            yield zit[i]




from itertools import count
import unittest

class InterleaveTests(unittest.TestCase):

    """Tests for interleave."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_empty_lists(self):
        self.assertIterableEqual(interleave([], []), [])

    def test_single_item_each(self):
        self.assertIterableEqual(interleave([1], [2]), [1, 2])

    def test_two_items_each(self):
        self.assertIterableEqual(interleave([1, 2], [3, 4]), [1, 3, 2, 4])

    def test_four_items_each(self):
        in1 = [1, 2, 3, 4]
        in2 = [5, 6, 7, 8]
        out = [1, 5, 2, 6, 3, 7, 4, 8]
        self.assertIterableEqual(interleave(in1, in2), out)

    def test_none_value(self):
        in1 = [1, 2, 3, None]
        in2 = [4, 5, 6, 7]
        out = [1, 4, 2, 5, 3, 6, None, 7]
        self.assertIterableEqual(interleave(in1, in2), out)

    def test_string_and_range(self):
        out = [0, 'H', 1, 'e', 2, 'l', 3, 'l', 4, 'o']
        self.assertIterableEqual(interleave(range(5), "Hello"), out)

    def test_with_generator(self):
        in1 = [1, 2, 3, 4]
        in2 = (n**2 for n in in1)
        out = [1, 1, 2, 4, 3, 9, 4, 16]
        self.assertIterableEqual(interleave(in1, in2), out)

    # Bonus 1
    # @unittest.expectedFailure
    def test_response_is_iterator(self):
        in1 = [1, 2, 3]
        in2 = [4, 5, 6]
        squares = (n**2 for n in in1)
        output = interleave(in1, in2)
        self.assertIs(iter(output), iter(output))
        output = interleave(squares, squares)
        self.assertEqual(next(output), 1)
        self.assertEqual(next(output), 4)
        self.assertEqual(next(squares), 9)
        iterator = interleave(count(), count())
        self.assertEqual(next(iterator), next(iterator))



    # # Bonus 2
    # # @unittest.expectedFailure
    def test_more_than_two_arguments(self):
        in1 = [1, 2, 3]
        in2 = [4, 5, 6]
        in3 = [7, 8, 9]
        out = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        self.assertIterableEqual(interleave(in1, in2, in3), out)


    # # Bonus 3
    # # @unittest.expectedFailure
    # def test_different_length_lists(self):
    #     in1 = [1, 2, 3]
    #     in2 = [4, 5, 6, 7, 8]
    #     in3 = [9]
    #     out1 = [1, 4, 9, 2, 5, 3, 6, 7, 8]
    #     self.assertIterableEqual(interleave(in1, in2, in3), out1)
    #     self.assertIterableEqual(
    #         interleave([1, 2], [3], [4, 5, 6], [7, 8], [9]),
    #         [1, 3, 4, 7, 9, 2, 5, 8, 6],
    #     )


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)

