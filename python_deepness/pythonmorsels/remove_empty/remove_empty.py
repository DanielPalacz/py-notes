
import os
import shutil
import sys


def __is_directory_empty(path: str) -> bool:
    return len(os.listdir(path)) == 0


def remove_empty(path_: str = ".") -> None:
    for directory in os.listdir(path_):
        full_path = os.path.join(path_, directory)

        if os.path.isdir(full_path):
            remove_empty(full_path)

    if __is_directory_empty(path_):
        print(f"Deleting directory {os.path.basename(path_)}")
        shutil.rmtree(path_)


if __name__ == "__main__":
    remove_empty(sys.argv[1])
