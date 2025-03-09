from unittest.mock import MagicMock

spy = MagicMock()

spy.do_something(1, 2)
spy.do_something(3, 4)

# Check how many times it was called
assert spy.do_something.call_count == 2
# Check the arguments it was called with
spy.do_something.assert_any_call(1, 2)
spy.do_something.assert_any_call(3, 4)
