import os
import shlex
import sys
import unittest
import warnings
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from importlib.util import spec_from_file_location, module_from_spec
from io import BytesIO, StringIO, TextIOWrapper
from pathlib import Path
from tempfile import NamedTemporaryFile
from textwrap import dedent


class TestFixNewLines(unittest.TestCase):

    """Tests for fix_newlines.py"""

    file1 = dedent("""
        Hello
        My name is Trey
        Welcome to my file
        This file is lovely
        Goodbye
    """).lstrip('\n')

    file2 = ""

    file3 = dedent("""
        Hello
        My name is Trey
        Welcome to my file
        This file is lovely
        Goodbye
    """).lstrip('\n').replace('\n', '\r\n')

    def test_file_with_newline_already(self):
        with make_file(self.file1) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_text(), f"{self.file1}")

    def test_add_newline_to_end(self):
        with make_file(self.file1.strip("\n")) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_text(), f"{self.file1}")

    def test_add_newline_to_end_of_empty_file(self):
        with make_file(self.file2) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_text(), f"{self.file2}\n")

    def test_different_line_endings_work(self):
        crlf_file = self.file3.strip("\r\n")
        lf_file = crlf_file.replace("\r\n", "\n")
        with make_file(crlf_file) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_text(), f"{lf_file}\n")

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_preserve_current_line_endings(self):
        crlf_bytes = self.file3.encode()

        # CRLF line endings preserved
        with make_file(crlf_bytes) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_bytes(), crlf_bytes)

        # No line ending added to end of file if it's missing
        with make_file(crlf_bytes.strip(b"\r\n")) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_bytes(), crlf_bytes)

        # LF line endings preserved
        lf_bytes = self.file1.encode()
        with make_file(lf_bytes) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(my_file.read_bytes(), lf_bytes)

    # To test bonus 2, comment out the next line
    @unittest.expectedFailure
    def test_fix_mixed_line_endings(self):
        mixed_ending_lf_bytes = (
            "This line ends in LF\n"
            "And this one end CRLF\r\n"
            "And this one ends in CRLF also\r\n"
            "Here's another line that ends in LF\n"
            "Here's another LF-ending line.\n"
        ).encode()

        # First/most common line ending used
        with make_file(mixed_ending_lf_bytes) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(
                my_file.read_bytes(),
                mixed_ending_lf_bytes.replace(b"\r\n", b"\n"),
            )

        mixed_ending_crlf_bytes = (
            "And this one end CRLF\r\n"
            "And this one ends in CRLF also\r\n"
            "\r\n"
            "This line ends in LF\n"
            "Here's another line that ends in CRLF\r\n"
        ).encode()

        # First/most common line ending used
        with make_file(mixed_ending_crlf_bytes) as my_file:
            run_program(f"fix_newlines.py {my_file}")
            self.assertEqual(
                my_file.read_bytes(),
                mixed_ending_crlf_bytes
                .replace(b"\r\n", b"\n")
                .replace(b"\n", b"\r\n"),
            )

    # To test bonus 3, comment out the next line
    @unittest.expectedFailure
    def test_print_lf_crlf_and_cr(self):
        mixed_ending_bytes = (
            "This line ends in LF\n"
            "And this one end CRLF\r\n"
            "And this one ends in CRLF also\r\n"
            "Here's another line that ends in LF\n"
            "Here's another LF-ending line.\n"
        ).encode()
        bytes_with_lf = mixed_ending_bytes.replace(b"\r\n", b"\n")
        bytes_with_crlf = bytes_with_lf.replace(b"\n", b"\r\n")

        # --print should print but not modify the file
        with make_file(mixed_ending_bytes) as my_file:
            output = run_program(f"fix_newlines.py --print {my_file}")
            self.assertEqual(output, bytes_with_lf.decode())
            self.assertEqual(my_file.read_bytes(), mixed_ending_bytes)

        # --crlf should convert all line endings to \r\n
        with make_file(mixed_ending_bytes) as my_file:
            run_program(f"fix_newlines.py --crlf {my_file}")
            self.assertEqual(my_file.read_bytes(), bytes_with_crlf)

        # --lf should convert all line endings to \n
        with make_file(mixed_ending_bytes) as my_file:
            run_program(f"fix_newlines.py --lf {my_file}")
            self.assertEqual(my_file.read_bytes(), bytes_with_lf)


try:
    DIRECTORY = Path(__file__).resolve().parent
except NameError:
    DIRECTORY = Path.cwd()


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(arguments, raises=DummyException, stderr=False):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.

    If stderr is True, separate stdout and stderr streams.
    """
    arguments = arguments.replace("\\", "\\\\")  # shlex posix=True workaround
    [path, *args] = shlex.split(arguments)
    path = str(DIRECTORY / path)
    old_args = sys.argv
    warnings.filterwarnings("ignore", r"unclosed file", ResourceWarning)
    warnings.filterwarnings("ignore", r"FileType is deprecated", PendingDeprecationWarning)
    try:
        sys.argv = [path, *args]  # Monkey-patch sys.argv
        with redirect_stdout(StringIO()) as output:
            error = StringIO() if stderr else output
            with redirect_stderr(error):
                try:
                    sys.modules.pop("__main__", None)
                    spec = spec_from_file_location("__main__", path)
                    module = module_from_spec(spec)
                    sys.modules["__main__"] = module
                    spec.loader.exec_module(module)
                # A specific exception should have been raised
                except raises as e:
                    # If sys.exit is called with a string, print it out
                    if isinstance(e, SystemExit):
                        if e.args and not isinstance(e.args[0], int):
                            if len(e.args) == 1:
                                error.write(str(e.args[0]))
                            else:
                                error.write(str(e.args))
                # An unexpected SystemExit exception was raised
                except SystemExit as e:
                    if e.args not in [(0,), (None,)]:
                        raise SystemExit(error.getvalue()) from e
                # No exception was raised
                else:
                    if raises is not DummyException:
                        raise AssertionError("{} not raised".format(raises))
                # Always force delete objects
                finally:
                    sys.modules["__main__"].__dict__.clear()
                    sys.modules.pop("__main__", None)  # Closes any open files

                if stderr:
                    return output.getvalue(), error.getvalue()
                else:
                    return output.getvalue()
    finally:
        sys.argv = old_args  # Undo the monkey patching of sys.argv


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wb', delete=False) as file:
        if contents:
            if isinstance(contents, str):
                contents = contents.encode('utf-8')
            file.write(contents)
    try:
        yield Path(file.name).resolve()
    finally:
        os.remove(file.name)


@contextmanager
def patch_stdin(text):
    real_stdin = sys.stdin
    if isinstance(text, str):
        text = text.encode(sys.stdin.encoding)
    sys.stdin = TextIOWrapper(
        PermanentBytesIO(text),
        encoding=sys.stdin.encoding,
        write_through=True,
    )
    try:
        yield sys.stdin
    except EOFError as e:
        raise AssertionError("Read more input than was given") from e
    finally:
        sys.stdin = real_stdin


class PermanentBytesIO(BytesIO):

    _closed = False

    def close(self):
        self._closed = True

    @property
    def closed(self):
        return self._closed


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import \
        python_version
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
