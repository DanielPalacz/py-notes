
# MagicMock = Mock + 'additional support for magic methods'
# Use Case: You should use MagicMock when you need to mock an object that uses special or magic methods


from unittest.mock import MagicMock

# Create a MagicMock object
magic_mock = MagicMock()

# Use magic methods
magic_mock.__getitem__.return_value = "mocked value"
magic_mock.__setitem__.return_value = None

# Call the magic methods
assert magic_mock['key'] == "mocked value"  # Magic method __getitem__ is called
magic_mock.__setitem__('key', 'value')  # Magic method __setitem__ is called

# Verifying that the magic methods were called
magic_mock.__getitem__.assert_called_once_with('key')
magic_mock.__setitem__.assert_called_once_with('key', 'value')