from typing import Any
from typing import Optional
from functools import wraps
from dataclasses import dataclass


NO_RETURN = object()


@dataclass
class Call:
    args: tuple
    kwargs: dict
    return_value: Any
    exception: Optional[Exception]


def record_calls(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return_value = f(*args, **kwargs)
            wrapper.calls.append(Call(args, kwargs, return_value, None))
            wrapper.call_count += 1
            return return_value

        except TypeError as e:
            wrapper.calls.append(Call(args, kwargs, NO_RETURN, e))
            wrapper.call_count += 1
            raise

        except Exception as e:
            wrapper.calls.append(Call(args, kwargs, NO_RETURN, e))
            wrapper.call_count += 1
            return NO_RETURN

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper



import unittest


class RecordCallsTests(unittest.TestCase):

    """Tests for record_calls."""

    def test_call_count_starts_at_zero(self):
        decorated = record_calls(lambda: None)
        self.assertEqual(decorated.call_count, 0)

    def test_not_called_on_decoration_time(self):
        def my_func():
            raise AssertionError("Function called too soon")
        record_calls(my_func)

    def test_function_still_callable(self):
        recordings = []
        def my_func():
            recordings.append('call')
        decorated = record_calls(my_func)
        self.assertEqual(recordings, [])
        decorated()
        self.assertEqual(recordings, ['call'])
        decorated()
        self.assertEqual(recordings, ['call', 'call'])

    def test_return_value(self):
        def one(): return 1
        one = record_calls(one)
        self.assertEqual(one(), 1)

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = record_calls(add)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)

    def test_takes_keyword_arguments(self):
        recordings = []
        @record_calls
        def my_func(*args, **kwargs):
            recordings.append((args, kwargs))
            return recordings
        self.assertEqual(my_func(), [((), {})])
        self.assertEqual(my_func(1, 2, a=3), [((), {}), ((1, 2), {'a': 3})])

    def test_call_count_increments(self):
        decorated = record_calls(lambda: None)
        self.assertEqual(decorated.call_count, 0)
        decorated()
        self.assertEqual(decorated.call_count, 1)
        decorated()
        self.assertEqual(decorated.call_count, 2)

    def test_different_functions(self):
        my_func1 = record_calls(lambda: None)
        my_func2 = record_calls(lambda: None)
        my_func1()
        self.assertEqual(my_func1.call_count, 1)
        self.assertEqual(my_func2.call_count, 0)
        my_func2()
        self.assertEqual(my_func1.call_count, 1)
        self.assertEqual(my_func2.call_count, 1)

    # Bonus 1
    # @unittest.expectedFailure
    def test_docstring_and_name_preserved(self):
        import pydoc
        decorated = record_calls(example)
        self.assertIn('example', str(decorated))
        # pydoc.render_doc does basically the same thing as help(...)
        documentation = pydoc.render_doc(decorated)
        self.assertIn('example', documentation)
        self.assertIn('This is a docstring, yay!', documentation)
        self.assertIn('(a, b=True)', documentation)

    # Bonus 2
    # @unittest.expectedFailure
    def test_record_arguments(self):
        @record_calls
        def my_func(*args, **kwargs): return args, kwargs
        self.assertEqual(my_func.calls, [])
        my_func()
        self.assertEqual(len(my_func.calls), 1)
        self.assertEqual(my_func.calls[0].args, ())
        self.assertEqual(my_func.calls[0].kwargs, {})
        my_func(1, 2, a=3)
        self.assertEqual(len(my_func.calls), 2)
        self.assertEqual(my_func.calls[1].args, (1, 2))
        self.assertEqual(my_func.calls[1].kwargs, {'a': 3})

    # Bonus 3
    # @unittest.expectedFailure
    def test_record_return_values(self):
        from record_calls import NO_RETURN
        @record_calls
        def my_func(*args, **kwargs): return sum(args), kwargs
        my_func()
        self.assertEqual(my_func.calls[0].return_value, (0, {}))
        my_func(1, 2, a=3)
        self.assertEqual(my_func.calls[1].return_value, (3, {'a': 3}))
        self.assertIs(my_func.calls[1].exception, None)
        with self.assertRaises(TypeError) as context:
            my_func(1, 'hi', a=3)
        self.assertIs(my_func.calls[2].return_value, NO_RETURN)
        self.assertEqual(my_func.calls[2].exception, context.exception)


def example(a, b=True):
    """This is a docstring, yay!"""
    print('hello world')


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
