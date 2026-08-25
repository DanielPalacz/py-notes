from time import time
from functools import wraps


def print_call_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time()
        ret = f(*args, **kwargs)

        print(f.__name__, "call time:", time() - t1, "seconds")
        return ret

    return wrapper


from io import StringIO
from contextlib import redirect_stdout
import re
from time import sleep
import unittest



# Regular expression to find a number followed by " seconds"
SECONDS_RE = re.compile(r"""
    (
        \d+             # Digits
        ( \. \d* )?     # Optional . with digits
        (e[+-]? \d+ )?  # Optional scientific notation
    )
    \s *                # Any whitespace
    seconds             # "seconds"
""", flags=re.VERBOSE)


class PrintCallTimeTests(unittest.TestCase):
    """Tests for the print_call_time decorator."""

    def test_return_value_preserved(self):
        """Decorated function returns the correct value."""
        @print_call_time
        def identity(x):
            return x

        @print_call_time
        def add(a, b):
            return a + b

        with redirect_stdout(StringIO()):
            self.assertEqual(identity(5), 5)
            self.assertEqual(identity("hello"), "hello")
            self.assertEqual(add(10, 3), 13)
            self.assertEqual(add(-1, 1), 0)

    def test_time_measured_is_plausible(self):
        """Measured time reflects the function's execution time."""
        sleep_duration = 0.1  # seconds

        @print_call_time
        def sleepy_function():
            sleep(sleep_duration)

        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            sleepy_function()

        output = output_buffer.getvalue().strip()

        self.assertRegex(
            output,
            SECONDS_RE,
            f"Output should contain time in seconds. Got: {output!r}"
        )

        # Extract the value to check plausibility
        match = SECONDS_RE.search(output)
        measured_time = float(match.group(1))
        self.assertGreaterEqual(measured_time, sleep_duration * 0.9)
        self.assertLess(measured_time, sleep_duration * 5)

    def test_multiple_calls(self):
        """Tests that output is produced for each call."""
        @print_call_time
        def counter_func():
            pass  # Do nothing

        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            counter_func()
            counter_func()
            counter_func()

        output = output_buffer.getvalue()
        matches = SECONDS_RE.findall(output)
        call_count = len(matches)
        self.assertEqual(
            call_count,
            3,
            f"Timing should print 3 times. {call_count} matches in:\n{output}",
        )

    def test_function_with_arguments(self):
        """Tests decorator on a function that accepts arguments."""
        @print_call_time
        def sum_list(numbers):
            return sum(numbers)

        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            result = sum_list([1, 2, 3, 4, 5])

        self.assertEqual(result, 15)
        output = output_buffer.getvalue().strip()
        self.assertRegex(
            output,
            SECONDS_RE,
            f"Output should contain time in seconds. Got: {output!r}"
        )

    def test_decorated_method(self):
        """Tests decorator on a method within a class."""
        class MyClass:
            def __init__(self, value):
                self.value = value

            @print_call_time
            def multiply(self, factor):
                sleep(0.01)
                return self.value * factor

        instance = MyClass(10)
        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            result = instance.multiply(5)

        self.assertEqual(result, 50)
        output = output_buffer.getvalue().strip()
        self.assertRegex(
            output,
            SECONDS_RE,
            f"Output should contain time in seconds. Got: {output!r}"
        )
        match = SECONDS_RE.search(output)
        measured_time = float(match.group(1))
        self.assertGreater(measured_time, 0.0, "Runtime should be positive")

    def test_function_with_own_print(self):
        """Tests that decorator print happens *after* function's own print."""
        @print_call_time
        def function_that_prints():
            print("Function executing")
            return "done"

        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            result = function_that_prints()

        self.assertEqual(result, "done")
        output = output_buffer.getvalue()

        self.assertTrue(
            output.startswith("Function executing\n"),
            "Function's own print should come first.",
        )
        self.assertRegex(
            output,
            SECONDS_RE,
            f"Timing line ('<time> seconds') not found in output: {output!r}"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
