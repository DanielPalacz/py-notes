import sys

FILENAME = sys.argv[1]
LINE_ENDINGS = ['\r\n', '\n']



class FixNewlines:
    def __init__(self, file: str = FILENAME):
        self.__filename = FILENAME
        self.__line_ending = None
        with open(self.__filename, mode='rt', encoding="utf-8", newline='') as file_r:
            self.file_text = file_r.read()
            self.ending = self.__detect_line_ending()

        self.ending = self.__detect_line_ending()
        self.is_ending_populated = self.file_text.endswith(('\r\n', '\n'))

    def run(self):

        if not bool(self.file_text):
            # Empty file, '\n' is not file ending - Incorrect Use Case 3 (empty file)
            self.__fix_lack_of_ending()

        elif self.is_ending_populated and self.ending in LINE_ENDINGS:
            # '\n' or '\r\n' is file ending character - Correct Use Case 1 (\n)
            #                                           Correct Use Case 5 (\r\n)
            # print("TAM3")
            pass

        else:
            # '\n' or '\r\n' is not file ending character - Incorrect Use Case 2
            self.__fix_lack_of_ending(end=self.ending)

    def __detect_line_ending(self) -> str:
        if '\r\n' in self.file_text:
            return '\r\n'
        else:
            return '\n'

    def __fix_lack_of_ending(self, end: str = '\n'):

        with open(self.__filename, mode='at', encoding="utf-8", newline='') as file_a:
            file_a.write(end)




fix_newlines_runner = FixNewlines()
fix_newlines_runner.run()
