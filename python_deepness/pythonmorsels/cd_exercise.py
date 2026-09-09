

import os
from tempfile import TemporaryDirectory
from typing import Optional


class cd:

    def __init__(self, subdir: Optional[str] = None):
        self._tmpdir = None

        if subdir is None:
            self._tmpdir = TemporaryDirectory()
            self.subdir = self._tmpdir.name
        else:
            self.subdir = subdir

        self._original = None

    def __enter__(self):
        self._original = os.getcwd()
        os.chdir(self.subdir)
        return self.subdir

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self._original)

        if self._tmpdir is not None:
            self._tmpdir.cleanup()



# with cd():
#     # print(Path('my_file.txt').read_text())
#     print("Inside With - 3")

# with cd("test1"):
#     print(Path('my_file.txt').read_text())
#     print("Inside With - 3")
#
# print("Program continues - 5")
#
#
#
# subdir1 = Path('test1')
# subdir2 = Path('test2')
