

from typing import Union
from pathlib import Path
from pathlib import PosixPath


def parent_directory(filepath: Union[Path, str], levels: int = 0) -> Union[PosixPath, Path, str]:
    p_ = Path(filepath)

    if p_.is_absolute():
        parent_ = p_.parent.absolute()
    else:
        parent_ = p_.parent

    if levels == 0:
        return parent_


    end_ = -1 * levels + 1
    len_path_tmp = len(str(parent_).split('/'))

    if str(parent_) == "/":
        len_path_tmp = 1
    elif len_path_tmp == 1 and not bool(str(parent_).count("/")):
        len_path_tmp = 0
    elif len_path_tmp == 1 and str(parent_).count("/") == 1:
        len_path_tmp = 1

    if not p_.is_absolute():
        if len_path_tmp < levels - 1:
            raise ValueError("It doesn't have enough parent directories.")

    elif p_.is_absolute():
        if len_path_tmp < levels:
            raise ValueError("It doesn't have enough parent directories.")

    elif not p_.is_absolute() and len_path_tmp < levels - 1:
        raise ValueError("It doesn't have enough parent directories.")


    if bool(end_):
        parent_tmp = "/".join(str(parent_).split('/')[0:end_:1])
    else:
        parent_tmp = "/".join(str(parent_).split('/')[0:])

    if p_.is_absolute() and parent_tmp and parent_tmp[0] != '/':
        return "/" + parent_tmp

    elif p_.is_absolute() and not parent_tmp:
        return "/"

    else:
        return parent_tmp




import os
import unittest
from pathlib import Path


class BaseTestCase(unittest.TestCase):

    def assertPathEqual(self, actual, expected):
        """Assert that two paths are equal when converted to strings."""
        actual_str = os.fspath(actual)
        expected_str = os.fspath(expected)
        if Path(actual_str) != Path(expected_str):
            self.fail(f"Expected path {expected_str!r} but got {actual_str!r}")


class ParentDirectoryTests(BaseTestCase):

    """Tests for parent_directory."""

    def test_string_path(self):
        self.assertPathEqual(
            parent_directory("/home/trey/stuff/script.py"),
            "/home/trey/stuff",
        )

    def test_path_object(self):
        self.assertPathEqual(
            parent_directory(Path("/home/trey/stuff/script.py")),
            "/home/trey/stuff",
        )

    def test_deeply_nested_path(self):
        self.assertPathEqual(
            parent_directory("/a/b/c/d/e/file.txt"),
            "/a/b/c/d/e",
        )
        self.assertPathEqual(
            parent_directory(Path("/a/b/c/d/e/file.txt")),
            "/a/b/c/d/e",
        )

    def test_root_directory(self):
        self.assertPathEqual(
            parent_directory("/file.txt"),
            "/",
        )
        self.assertPathEqual(
            parent_directory(Path("/file.txt")),
            "/",
        )

    def test_relative_path(self):
        self.assertPathEqual(
            parent_directory("stuff/script.py"),
            "stuff",
        )
        self.assertPathEqual(
            parent_directory(Path("stuff/script.py")),
            "stuff",
        )

    def test_current_directory(self):
        self.assertPathEqual(
            parent_directory("file.txt"),
            ".",
        )
        self.assertPathEqual(
            parent_directory(Path("file.txt")),
            ".",
        )


# Bonus 1
# @unittest.expectedFailure
class Bonus1Tests(BaseTestCase):
    """Tests for bonus 1: levels parameter."""

    def test_levels_two(self):
        self.assertPathEqual(
            parent_directory("/home/trey/stuff/script.py", levels=2),
            "/home/trey",
        )
        self.assertPathEqual(
            parent_directory(Path("/home/trey/stuff/script.py"), levels=2),
            "/home/trey",
        )

    def test_levels_three(self):
        self.assertPathEqual(
            parent_directory("/home/trey/stuff/script.py", levels=3),
            "/home",
        )

    def test_levels_four(self):
        self.assertPathEqual(
            parent_directory(Path("/home/trey/stuff/script.py"), levels=4),
            "/",
        )

    def test_levels_one_explicit(self):
        self.assertPathEqual(
            parent_directory("/home/trey/stuff/script.py", levels=1),
            "/home/trey/stuff",
        )

    def test_levels_relative_path_string(self):
        self.assertPathEqual(
            parent_directory("a/b/c/d/file.txt", levels=2),
            "a/b/c",
        )
        self.assertPathEqual(
            parent_directory("a/b/c/d/file.txt", levels=3),
            "a/b",
        )

    def test_levels_relative_path_object(self):
        self.assertPathEqual(
            parent_directory(Path("a/b/c/d/file.txt"), levels=2),
            "a/b/c",
        )
        self.assertPathEqual(
            parent_directory(Path("a/b/c/d/file.txt"), levels=3),
            "a/b",
        )


# Bonus 2
# @unittest.expectedFailure
class Bonus2Tests(BaseTestCase):
    """Tests for bonus 2: raise ValueError when levels exceeds path depth."""

    def test_too_many_levels_absolute(self):
        with self.assertRaises(ValueError):
            parent_directory("/home/trey/stuff/script.py", levels=5)

    def test_max_valid_levels_absolute(self):
        self.assertPathEqual(
            parent_directory("/home/trey/stuff/script.py", levels=4),
            "/",
        )

    def test_too_many_levels_relative(self):
        with self.assertRaises(ValueError):
            parent_directory("trey/stuff/script.py", levels=4)

    def test_max_valid_levels_relative(self):
        self.assertPathEqual(
            parent_directory("trey/stuff/script.py", levels=3),
            ".",
        )

    def test_too_many_levels_single_component_relative(self):
        with self.assertRaises(ValueError):
            parent_directory("file.txt", levels=2)

    def test_too_many_levels_root_absolute(self):
        with self.assertRaises(ValueError):
            parent_directory("/file.txt", levels=2)

    def test_error_is_value_error(self):
        with self.assertRaises(ValueError):
            parent_directory("a/b/c.txt", levels=4)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 9):
        sys.exit(f"Running {python_version()}.  Python 3.9 required.")
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
