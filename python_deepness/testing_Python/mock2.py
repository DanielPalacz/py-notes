from unittest.mock import Mock

# Create a mock object
my_mock = Mock()

# Set return value for a method
my_mock.some_method.return_value = "Hello, World!"

# Call the method
result = my_mock.some_method()

# Assert that the method was called
my_mock.some_method.assert_called_once()
assert result == "Hello, World!"

# In this example, Mock is sufficient because we're just calling methods and verifying interactions.
