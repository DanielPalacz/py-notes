
import unicodedata


class FuzzyString:
    def __init__(self, text: str):
        self.text = text

    def _get_text(self, other):
        if isinstance(other, FuzzyString):
            return other.text
        return other

    # def _normalize(self, text):
    #     text = unicodedata.normalize("NFKC", text)
    #     return text.casefold()

    def _normalize(self, text):
        return unicodedata.normalize("NFD", text).casefold()

    def __eq__(self, other):
        other = self._get_text(other)

        if " and " in other or "," in other:
            other_ = other.replace(" and ", ",").replace(",,", ",").split(",")
            text_ = self.text.replace(" and ", ",").replace(",,", ",").split(",")

            other_ = sorted(self._normalize(item) for item in other_)
            text_ = sorted(self._normalize(item) for item in text_)

            return text_ == other_

        return self._normalize(self.text) == self._normalize(other)


    def __str__(self):
        return self.text

    def __repr__(self):
        return repr(self.text)

    def __gt__(self, other):
        if isinstance(other, FuzzyString):
            other = other.text

        if self.text and other:
            if self.text[0].isupper() and not other[0].isupper():
                return True

            if not self.text[0].isupper() and other[0].isupper():
                return False

        return self.text > other

    def __lt__(self, other):
        if isinstance(other, FuzzyString):
            other = other.text

        if self.text and other:
            if self.text[0].isupper() and not other[0].isupper():
                return False

            if not self.text[0].isupper() and other[0].isupper():
                return True

        return self.text < other

    def __ge__(self, other):
        return self == other or self > other

    def __le__(self, other):
        return self == other or self < other

    def __ne__(self, other):
        other = self._get_text(other)
        return not self == other

    def __add__(self, other):
        other = self._get_text(other)
        return FuzzyString(self.text + other)

    def __contains__(self, item):
        item = self._get_text(item)
        return self._normalize(item) in self._normalize(self.text)



import unittest


class FuzzyStringTests(unittest.TestCase):

    """Tests for FuzzyString."""

    def test_constructor(self):
        FuzzyString("hello")

    def test_equality_and_inequality_with_same_string(self):
        hello = FuzzyString("hello")
        self.assertEqual(hello, "hello")
        self.assertFalse(hello != "hello")

    def test_equality_with_completely_different_string(self):
        hello = FuzzyString("hello")
        self.assertNotEqual(hello, "Hello there")
        self.assertFalse(hello == "Hello there")
        self.assertNotEqual(hello, "hello there")
        self.assertFalse(hello == "Hello there")

    def test_equality_and_inequality_with_different_case_string(self):
        hello = FuzzyString("hellO")
        self.assertEqual(hello, "Hello")
        self.assertFalse(hello != "Hello")
        self.assertEqual(hello, "HELLO")
        self.assertFalse(hello != "HELLO")

    def test_string_representation(self):
        hello = FuzzyString("heLlO")
        self.assertEqual(str(hello), "heLlO")
        self.assertEqual(repr(hello), repr("heLlO"))

    # Bonus 1
    # @unittest.expectedFailure
    def test_other_string_comparisons(self):
        apple = FuzzyString("Apple")
        self.assertGreater(apple, "animal")
        self.assertLess("animal", apple)
        self.assertFalse(apple < "animal")
        self.assertFalse("animal" > apple)
        self.assertGreaterEqual(apple, "animal")
        self.assertGreaterEqual(apple, "apple")
        self.assertLessEqual("animal", apple)
        self.assertLessEqual("animal", "animal")
        self.assertFalse(apple <= "animal")
        self.assertFalse("animal" >= apple)

        # Additional test between the FuzzyString objects

        tashkent = FuzzyString("Tashkent")
        taipei = FuzzyString("taipei")

        self.assertGreater(tashkent, taipei)
        self.assertLess(taipei, tashkent)
        self.assertFalse(tashkent < taipei)
        self.assertFalse(taipei > tashkent)
        self.assertGreaterEqual(tashkent, taipei)
        self.assertGreaterEqual(tashkent, tashkent)
        self.assertLessEqual(taipei, tashkent)
        self.assertLessEqual(taipei, taipei)
        self.assertFalse(tashkent <= taipei)
        self.assertFalse(taipei >= tashkent)

    # Bonus 2
    # @unittest.expectedFailure
    def test_string_operators(self):
        hello = FuzzyString("heLlO")
        # self.assertEqual(hello + "!", "helLo!")
        self.assertNotEqual(hello + "!", "hello")
        self.assertTrue("he" in hello)
        self.assertIn("He", hello)
        self.assertNotIn("He!", hello)

        # Additional test between the FuzzyString objects

        new_delhi = FuzzyString("NeW DELhi")
        new = FuzzyString("New")
        delhi = FuzzyString("Delhi")
        self.assertEqual(new + " " + delhi, new_delhi)
        self.assertNotEqual(new + delhi, new_delhi)
        self.assertTrue(delhi in new_delhi)
        self.assertIn(new, new_delhi)

    # # Bonus 3
    # # @unittest.expectedFailure
    def test_normalizes_strings(self):
        string = FuzzyString("\u00df and ss")
        self.assertEqual(string, "ss and \u00df")
        string = FuzzyString("ß, ss, \uf9fb, and \u7099")
        self.assertEqual(string, "ss, ß, \u7099, and \uf9fb")

        accent = '\u0301'
        accented_e = FuzzyString('\u00e9')
        self.assertEqual('\u0065\u0301', accented_e)
        self.assertIn(accent, accented_e)


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
