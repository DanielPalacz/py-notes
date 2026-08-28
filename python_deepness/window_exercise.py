from typing import Iterable, Iterator


def window(numbers: Iterable, n: int) -> Iterator[tuple]:
    iterator = iter(numbers)

    window_items = []
    window_items_tmp = []
    for number in iterator:
        window_items.append(number)
        window_items_tmp.append(number)

        if len(window_items) == n:
            yield tuple(window_items)
            window_items.pop(0)
    # else:

    if not window_items_tmp and n:
        for _ in range(0, n):
            window_items.append(None)
        yield tuple(window_items)


# from typing import Iterable, Iterator
#
#
# def window(numbers: Iterable, n: int) -> Iterator[tuple]:
#     iterator = iter(numbers)
#
#     window_items = []
#     # it_lenght = 0
#     for number in iterator:
#         window_items.append(number)
#
#         if len(window_items) == n:
#             yield tuple(window_items)
#             window_items.pop(0)
#

nums = [1, 2, 3, 4, 5, 6]
# w_numbers = window(nums, 2)
w_numbers = window(nums, 3)


import unittest


class WindowTests(unittest.TestCase):

    """Tests for window."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_window_size_2(self):
        inputs = [1, 2, 3]
        outputs = [(1, 2), (2, 3)]
        self.assertIterableEqual(window(inputs, 2), outputs)

    def test_window_size_1(self):
        self.assertIterableEqual(window([1, 2, 3], 1), [(1,), (2,), (3,)])
        self.assertIterableEqual(window([1], 1), [(1,)])

    def test_none(self):
        inputs = [None, None]
        outputs = [(None, None)]
        self.assertIterableEqual(window(inputs, 2), outputs)

    def test_string(self):
        inputs = "hey"
        outputs = [('h', 'e'), ('e', 'y')]
        self.assertIterableEqual(window(inputs, 2), outputs)

    def test_window_size_3(self):
        inputs = [1, 2, 3, 4, 5, 6]
        outputs = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
        self.assertIterableEqual(window(inputs, 3), outputs)

    def test_window_size_0(self):
        self.assertIterableEqual(window([1, 2, 3], 0), [])
        self.assertIterableEqual(window([], 0), [])

    def test_accepts_iterator(self):
        inputs = (n**2 for n in [1, 2, 3, 4])
        outputs = [(1, 4), (4, 9), (9, 16)]
        self.assertIterableEqual(window(inputs, 2), outputs)

    # Bonus 1
    # @unittest.expectedFailure
    def test_returns_lazy_iterable(self):
        inputs = (n**2 for n in [1, 2, 3, 4, 5])
        iterable = window(inputs, 2)
        self.assertEqual(iter(iterable), iter(iterable))
        self.assertEqual(next(iterable), (1, 4))
        self.assertEqual(next(inputs), 9)
        self.assertEqual(list(iterable), [(4, 16), (16, 25)])

    # Bonus 2
    # @unittest.expectedFailure
    def test_window_size_larger_than_iterable(self):
        self.assertIterableEqual(window([], 1), [(None,)])
        self.assertIterableEqual(window([1, 2], 3), [(1, 2, None,)])
        self.assertIterableEqual(window([1, 2, 3], 4), [(1, 2, 3, None)])

    # # Bonus 3
    # # @unittest.expectedFailure
    # def test_fillvalue_as_keyword_argument_only(self):
    #     """Test can be called with fillvalue (but only as keyword arg)."""
    #     inputs = [1, 2, 3]
    #     outputs = [(1, 2, 3, 0)]
    #     self.assertIterableEqual(window(inputs, 4, fillvalue=0), outputs)
    #     with self.assertRaises(TypeError):
    #         window(inputs, 4, 0)


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
