from typing import Optional
import random


class RandomLooper:
    def __init__(self, iterable_obj: Optional[list] = None, *args):
        if iterable_obj is None:
            self.iterable_obj = []
        else:
            self.iterable_obj = list(iterable_obj)

        for args_iterable_obj in args:
            self.iterable_obj += args_iterable_obj


    def __call__(self):
        return iter(self.iterable_obj)

    def __iter__(self):
        items = list(self.iterable_obj)
        random.shuffle(items)

        length = len(self)

        if length == 0:
            return

        tmp = 0

        while tmp < length:
            yield items[tmp]
            tmp += 1

    def __len__(self):
        return len(self.iterable_obj)



import unittest


class RandomLooperTests(unittest.TestCase):

    """Tests for RandomLooper."""

    def test_constructor(self):
        RandomLooper([1, 2, 3, 4])

    def test_empty_iterable(self):
        looper = RandomLooper(())
        self.assertEqual(list(looper), [])

    def test_one_item(self):
        looper = RandomLooper({1})
        self.assertEqual(list(looper), [1])

    def test_loop_once(self):
        looper = RandomLooper([1, 2, 3, 4])
        self.assertEqual(set(looper), {1, 2, 3, 4})

    def test_original_unchanged(self):
        numbers = [1, 2, 3, 4]
        looper = RandomLooper(numbers)
        list(looper)
        self.assertEqual(numbers, [1, 2, 3, 4])

    # Bonus 1
    # @unittest.expectedFailure
    def test_length(self):
        looper = RandomLooper(range(1000))
        self.assertEqual(len(looper), 1000)
        looper = RandomLooper('hello')
        self.assertEqual(len(looper), 5)

    # Bonus 2
    # @unittest.expectedFailure
    def test_accepts_multiple_iterables(self):
        self.assertEqual(
            set(RandomLooper([1, 2], 'hey')),
            {1, 2, 'h', 'e', 'y'},
        )
        fives = [5] * 1000
        threes = [3]
        many_first_items = [
            next(iter(RandomLooper(fives, threes)))
            for _ in range(100)
        ]
        three_count = len([
            item
            for item in many_first_items
            if item == 3
        ])
        self.assertLess(three_count, 15)

    # Bonus 3
    # @unittest.expectedFailure
    def test_looping_multiple_times(self):
        looper = RandomLooper(range(1000))
        loop1, loop2 = list(looper), list(looper)
        self.assertNotEqual(loop1, loop2)
        looper3 = RandomLooper([1, 2, 3])
        orders = {
            tuple(looper3)
            for _ in range(100)
        }
        self.assertEqual(orders, {
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        })


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
