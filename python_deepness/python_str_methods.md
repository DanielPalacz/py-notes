| Method         | Requires Arguments           | Description                                                                 |
|----------------|------------------------------|-----------------------------------------------------------------------------|
| capitalize     | No                           | Returns a copy of the string with its first character capitalized.         |
| casefold       | No                           | Returns a casefolded copy of the string, used for caseless comparisons.    |
| center         | Yes                          | Returns a centered string of a given width.                                |
| count          | Yes                          | Returns the number of non-overlapping occurrences of a substring.          |
| encode         | No                           | Encodes the string using the default encoding (UTF-8).                     |
| endswith       | Yes                          | Returns True if the string ends with the specified suffix.                 |
| expandtabs     | No                           | Replaces tab characters with spaces.                                       |
| find           | Yes                          | Returns the lowest index where the substring is found, or -1 if not found. |
| format         | No                           | Formats the string using positional and keyword arguments.                 |
| format_map     | Yes                          | Formats using a mapping object.                                            |
| index          | Yes                          | Like `find()`, but raises ValueError if the substring is not found.        |
| isalnum        | No                           | Returns True if all characters are alphanumeric.                           |
| isalpha        | No                           | Returns True if all characters are alphabetic.                             |
| isascii        | No                           | Returns True if all characters are ASCII.                                  |
| isdecimal      | No                           | Returns True if all characters are decimal characters.                     |
| isdigit        | No                           | Returns True if all characters are digits.                                 |
| isidentifier   | No                           | Returns True if the string is a valid identifier.                          |
| islower        | No                           | Returns True if all cased characters are lowercase.                        |
| isnumeric      | No                           | Returns True if all characters are numeric characters.                     |
| isprintable    | No                           | Returns True if all characters are printable or the string is empty.       |
| isspace        | No                           | Returns True if all characters are whitespace.                             |
| istitle        | No                           | Returns True if the string is titlecased.                                  |
| isupper        | No                           | Returns True if all cased characters are uppercase.                        |
| join           | Yes                          | Concatenates an iterable of strings using the string as a separator.       |
| ljust          | Yes                          | Returns a left-justified string of a given width.                          |
| lower          | No                           | Returns a copy of the string in lowercase.                                 |
| lstrip         | No                           | Returns a copy of the string with leading whitespace removed.              |
| maketrans      | Yes                          | Returns a translation table usable for `translate()`.                      |
| partition      | Yes                          | Splits the string at the first occurrence of the separator.                |
| removeprefix   | Yes                          | Returns a string with the specified prefix removed, if present.            |
| removesuffix   | Yes                          | Returns a string with the specified suffix removed, if present.            |
| replace        | Yes                          | Returns a copy with all occurrences of a substring replaced.               |
| rfind          | Yes                          | Returns the highest index of the substring, or -1 if not found.            |
| rindex         | Yes                          | Like `rfind()` but raises ValueError if the substring is not found.        |
| rjust          | Yes                          | Returns a right-justified string of a given width.                         |
| rpartition     | Yes                          | Splits the string at the last occurrence of the separator.                 |
| rsplit         | No                           | Splits the string from the right using a separator.                        |
| rstrip         | No                           | Returns a copy of the string with trailing whitespace removed.             |
| split          | No                           | Splits the string using a separator.                                       |
| splitlines     | No                           | Splits the string at line breaks.                                          |
| startswith     | Yes                          | Returns True if the string starts with the specified prefix.               |
| strip          | No                           | Returns a copy of the string with leading and trailing whitespace removed. |
| swapcase       | No                           | Swaps case of all characters in the string.                                |
| title          | No                           | Returns a titlecased version of the string.                                |
| translate      | Yes                          | Translates characters using a translation table.                           |
| upper          | No                           | Returns a copy of the string in uppercase.                                 |
| zfill          | Yes                          | Pads the string on the left with zeros to fill a given width.             |
