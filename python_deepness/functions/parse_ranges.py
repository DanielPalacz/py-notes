import tracemalloc
import unittest
from collections.abc import Iterator

S1 = '1-2,4-4,8-13'
S2 = '0-0, 4-8, 20-20, 43-45'


def parse_ranges(text: str) -> Iterator[int]:
    ranges_list = text.split(',')

    numbers = []
    for range_str in ranges_list:

        try:
            if "->exit" not in range_str:
                start_num, end_num = range_str.split('-')
            else:
                start_num = int(range_str.replace('->exit', ''))
                end_num = start_num

        except ValueError:
            start_num = int(range_str)
            end_num = int(range_str)

        for number in range(int(start_num), int(end_num) + 1):
            yield number


class ParseRangesTests(unittest.TestCase):

    """Tests for parse_ranges."""

    def test_three_ranges(self):
        self.assertEqual(
            list(parse_ranges('1-2,4-4,8-10')),
            [1, 2, 4, 8, 9, 10],
        )

    def test_with_spaces(self):
        self.assertEqual(
            list(parse_ranges('0-0, 4-8, 20-21, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45],
        )

    # Bonus 1
    # @unittest.expectedFailure
    def test_return_iterator(self):
        numbers = parse_ranges('0-0, 4-8, 20-21, 43-45')
        self.assertEqual(next(numbers), 0)
        self.assertEqual(list(numbers), [4, 5, 6, 7, 8, 20, 21, 43, 44, 45])
        self.assertEqual(list(numbers), [])

        # Test memory usage for a long iterable
        tracemalloc.start()
        numbers = parse_ranges('1-5000')
        before = tracemalloc.take_snapshot()
        # Consume some items
        for _ in range(50):
            next(numbers)
        after = tracemalloc.take_snapshot()
        top_stats = after.compare_to(before, 'lineno')
        total_size = sum(stat.size for stat in top_stats)
        raise ValueError(total_size)
        self.assertLess(total_size, 3000, "Memory usage is too high")

        tracemalloc.stop()


    # Bonus 2
    # @unittest.expectedFailure
    def test_with_individual_numbers(self):
        self.assertEqual(
            list(parse_ranges('0,4-8,20,43-45')),
            [0, 4, 5, 6, 7, 8, 20, 43, 44, 45],
        )

    # Bonus 3
    # @unittest.expectedFailure
    def test_ignore_arrows(self):
        self.assertEqual(
            list(parse_ranges('0, 4-8, 20->exit, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 43, 44, 45],
        )

class ColoredTestResult(unittest.TextTestResult):

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    def addSuccess(self, test):
        super().addSuccess(test)
        if self.showAll:
            self.stream.writeln(
                f"{self.GREEN}ok{self.RESET}"
            )

    def printErrorList(self, flavour, errors):
        if flavour == "FAIL":
            colour = self.RED
        elif flavour == "ERROR":
            colour = self.RED
        elif flavour == "ok":
            colour = self.GREEN
        elif flavour == "OK":
            colour = self.GREEN
        else:
            colour = self.YELLOW

        for test, err in errors:
            self.stream.writeln(
                f"{colour}{flavour}: {test}{self.RESET}"
            )
            self.stream.writeln(err)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""

    class resultclass(ColoredTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys

    if sys.version_info < (3, 6):
        sys.exit(
            "Running {}. Python 3.6 required.".format(python_version())
        )

    unittest.main(
        verbosity=2,
        testRunner=AllowUnexpectedSuccessRunner
    )