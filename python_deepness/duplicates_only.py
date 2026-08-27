from collections import Counter


def duplicates_only(iterable):
    data_counter = Counter(iterable)
    return [d[0] for d in data_counter.items() if d[1] > 1]



from random import randint
from time import perf_counter_ns
import timeit
import unittest


class DuplicatesOnlyTests(unittest.TestCase):

    def assertLessThanFactor(self, large, small, factor, required_factor=2.0):
        """Assert that large is not too much slower than small."""
        # This assertion MUST pass
        self.assertLess(large, small*factor*required_factor)
        try:
            self.assertLess(large, small*factor)
        except AssertionError as e:
            raise FlakyAssertionError(f"{large} >= {small}*{factor}!") from e
            self.assertLess(large, small*factor)

    def assertItemsEqual(self, iterable1, iterable2):
        """Assert that iterables have same items, but ignore the order."""
        self.assertEqual(sorted(iterable1), sorted(iterable2))

    def test_with_duplicates(self):
        self.assertItemsEqual(duplicates_only([2, 1, 3, 2, 4, 3]), [2, 3])

    def test_empty_iterable(self):
        self.assertItemsEqual(duplicates_only([]), [])

    def test_no_duplicates(self):
        self.assertItemsEqual(duplicates_only([2, 1, 3, 4, 7, 11, 18]), [])

    def test_multiple_duplicates(self):
        self.assertItemsEqual(duplicates_only([2, 1, 3, 4, 3, 7, 11, 3]), [3])

    def test_different_item_types(self):
        self.assertItemsEqual(
            duplicates_only(["red", "blue", "red", "green", "yellow", "blue"]),
            ["red", "blue"],
        )
        self.assertItemsEqual(
            duplicates_only([(1, 2), (2, 1), (3, 4), (1, 2), (4, 3)]),
            [(1, 2)],
        )

    def test_different_iterable_types(self):
        self.assertItemsEqual(duplicates_only((2, 1, 3, 2, 2, 3, 4)), [2, 3])
        self.assertItemsEqual(duplicates_only(range(5)), [])

    def test_performance(self):
        n, m, p, q = 3.0, 2.4, 2.2, 2.2
        # Create large lists, each double the size of the last
        micro_numbers = [randint(1, 500) for _ in range(256)]
        tiny_numbers = [randint(1, 500) for _ in range(512)]
        small_numbers = [randint(1, 500) for _ in range(1_024)]
        medium_numbers = [randint(1, 500) for _ in range(2_048)]
        large_numbers = [randint(1, 500) for _ in range(4_096)]
        huge_numbers = [randint(1, 500) for _ in range(8_192)]
        micro_time = tiny_time = small_time = medium_time = large_time = 0

        # The attempt_n_times decorator automatically runs this block N times,
        # raising an exception only if all attempted runs fail
        @attempt_n_times(15)
        def _():
            nonlocal micro_time, tiny_time
            micro_time = time(micro_numbers)
            tiny_time = time(tiny_numbers)
            self.assertLessThanFactor(tiny_time, micro_time, n)

        @attempt_n_times(12)
        def _():
            nonlocal small_time
            small_time = time(small_numbers)
            self.assertLessThanFactor(small_time, micro_time, n*m)
            self.assertLessThanFactor(small_time, tiny_time, n)

        @attempt_n_times(12)
        def _():
            nonlocal medium_time
            medium_time = time(medium_numbers)
            self.assertLessThanFactor(medium_time, micro_time, n*m*p, 2.2)
            self.assertLessThanFactor(medium_time, tiny_time, n*m)
            self.assertLessThanFactor(medium_time, small_time, n)

        @attempt_n_times(10)
        def _():
            nonlocal large_time
            large_time = time(large_numbers)
            self.assertLessThanFactor(large_time, micro_time, n*m*p*q, 2.5)
            self.assertLessThanFactor(large_time, tiny_time, n*m*p, 2.2)
            self.assertLessThanFactor(large_time, small_time, n*m, 2.0)
            self.assertLessThanFactor(large_time, medium_time, n, 2.0)

        @attempt_n_times(8)
        def _():
            huge_time = time(huge_numbers)
            self.assertLessThanFactor(large_time, tiny_time, n*m*p*q, 2.5)
            self.assertLessThanFactor(huge_time, small_time, n*m*p, 2.2)
            self.assertLessThanFactor(huge_time, medium_time, n*m, 2.0)
            self.assertLessThanFactor(huge_time, large_time, n, 2.0)

    # Bonus 1
    # @unittest.expectedFailure
    def test_order_is_maintained(self):
        self.assertEqual(list(duplicates_only([2, 1, 3, 4, 3, 2, 3])), [2, 3])
        self.assertEqual(list(duplicates_only("LETTERSWORKTOO")), list("ETRO"))


class FlakyAssertionError(AssertionError):
    """Assertion error raised when a "flaky" assertion is being made."""


def attempt_n_times(n):
    """
    Run tests multiple times if assertions are raised.

    Allows for more forgiving tests when assertions may be a bit flaky.
    """
    def decorator(function):
        """This looks like a decorator, but it actually runs the function!"""
        def block_wrapper():
            for attempts_left in reversed(range(n)):
                try:
                    return function()
                except FlakyAssertionError:
                    if attempts_left == 0:
                        raise
        return block_wrapper()
    return decorator


def auto_time(code, *, setup="", globals, repeat=7, number=1, threshold=10000):
    """
    Return the time the given code takes to run.

    Runs code until total time is greater than the threshold (in nanoseconds).

    Fast-fail for algorithms that are too slow on small inputs.
    """
    timer = timeit.Timer(code, setup, perf_counter_ns, globals)
    time_taken = min(timer.repeat(repeat, number))

    # Fast-fail: if even a single run takes too long, it's a bad algorithm
    if time_taken > 50_000_000:  # 50ms for single run is way too slow
        return time_taken/number

    while time_taken < threshold:
        number *= 2
        time_taken = min(timer.repeat(repeat, number))
        # Another fast-fail check as we scale up
        if time_taken/number > 10_000_000:  # 10ms per operation is too slow
            break
    return time_taken/number


def time(iterable):
    try:
        return auto_time(
            "duplicates_only(iterable)",
            repeat=15,  # Reduced repeats for faster fail-out
            threshold=30_000,
            globals={
                "duplicates_only": duplicates_only,
                "iterable": iterable,
            },
        )
    except Exception:
        # If timing fails completely, return a very large time to ensure test failure
        return 999_999_999


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

