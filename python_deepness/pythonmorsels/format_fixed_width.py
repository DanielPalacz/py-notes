


rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]

# rows = [["Jane"], ["Mark"]]


from typing import Optional

def format_fixed_width(rows_of_columns: list[list], widths: Optional[list] = None, padding: int = 2) -> str:
    if widths is None:
        columns_width = []
        for col in zip(*rows_of_columns):
            column_width = len(max(col, key=len)) + padding
            columns_width.append(column_width)
    else:
        columns_width = [num + padding for num in widths]

    text = ""

    for row in rows_of_columns:
        words = ""

        for word, column_width in zip(row, columns_width):
            spaces = (column_width - len(word)) * " "
            words += word + spaces

        text += words.rstrip() + "\n"

    return text.rstrip()



OUTPUT = format_fixed_width(rows)


from textwrap import dedent
import unittest


class FormatFixedWidthTests(unittest.TestCase):

    """Tests for format_fixed_width."""

    def test_single_list_with_single_element(self):
        self.assertEqual(format_fixed_width([["hello"]]), "hello")

    def test_single_list_with_two_elements(self):
        self.assertEqual(format_fixed_width([["hi", "there"]]), "hi  there")

    def test_two_lists_with_one_element_each(self):
        self.assertEqual(
            format_fixed_width([["Jane"], ["Mark"]]),
            "Jane\nMark"
        )

    def test_two_lists_with_two_elements_each(self):
        self.assertEqual(
            format_fixed_width([["Jane", "Austen"], ["Mark", "Twain"]]),
            dedent("""
                Jane  Austen
                Mark  Twain
            """).strip("\n")
        )

    def test_no_rows(self):
        self.assertEqual(format_fixed_width([]), "")

    def test_different_length_first_column(self):
        self.assertEqual(
            format_fixed_width([
                ["Jane", "Austen"],
                ["Mark", "Twain"],
                ["Charlotte", "Brontë"]
            ]),
            dedent("""
                Jane       Austen
                Mark       Twain
                Charlotte  Brontë
            """).strip("\n")
        )

    def test_missing_column_data(self):
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ]),
            dedent("""
                Jane               Austen
                Samuel  Langhorne  Clemens
                        Charlotte  Brontë
            """).strip("\n")
        )

    # Bonus 1
    @unittest.expectedFailure
    def test_different_padding(self):
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], padding=1),
            dedent("""
                Jane             Austen
                Samuel Langhorne Clemens
                       Charlotte Brontë
            """).strip("\n")
        )
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], padding=3),
            dedent("""
                Jane                 Austen
                Samuel   Langhorne   Clemens
                         Charlotte   Brontë
            """).strip("\n")
        )

    # Bonus 2
    # @unittest.expectedFailure
    def test_column_widths_specified(self):
        self.assertEqual(
            format_fixed_width([
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], widths=[10, 10, 10]),
            dedent("""
                Samuel      Langhorne   Clemens
                            Charlotte   Brontë
            """).strip("\n")
        )
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], widths=[8, 10, 10], padding=1),
            dedent("""
                Jane                Austen
                Samuel   Langhorne  Clemens
                         Charlotte  Brontë
            """).strip("\n")
        )

    # # Bonus 3
    # # @unittest.expectedFailure
    # def test_column_alignments(self):
    #     self.assertEqual(
    #         format_fixed_width([
    #             ['NN', 'Artist', 'Title', 'Time'],
    #             ['03', 'Paul Simon', 'Peace Like a River', '3:23'],
    #             ['16', 'Johnny Cash', 'Personal Jesus', '3:20'],
    #             ['', '', '', '1:09:32']
    #         ], alignments=['L', 'L', 'L', 'R']),
    #         dedent("""
    #             NN  Artist       Title                  Time
    #             03  Paul Simon   Peace Like a River     3:23
    #             16  Johnny Cash  Personal Jesus         3:20
    #                                                  1:09:32
    #         """).strip("\n")
    #     )


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

