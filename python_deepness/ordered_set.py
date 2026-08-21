from collections.abc import Mapping, Iterable
from functools import partial
from itertools import islice
from sys import getsizeof
from textwrap import dedent
from time import perf_counter_ns
import timeit
import unittest


from collections import Counter


class OrderedSet:
    def __init__(self, words_list: list|str):

        if isinstance(words_list, str):
            if ' ' not in words_list:
                self.ordered_words = words_list
                return None


        self.data_are_int_only = True

        self.ordered_words = []
        counter_data = Counter(words_list)
        for word, word_count in counter_data.items():
            self.ordered_words.append(word)
            if self.data_are_int_only and not isinstance(word, int):
                self.data_are_int_only = False


    def __add__(self, other):
        if other not in self.ordered_words:
            self.ordered_words.append(other)

    add = __add__

    def __contains__(self, item):
        if self.data_are_int_only:
            if list(range(len(self.ordered_words))) == list(set(self.ordered_words)):
                return item < self.ordered_words[-1]

        return item in self.ordered_words

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.ordered_words == other.ordered_words

        if isinstance(other, list):
            return self.ordered_words == other

        if isinstance(other, set):
            return set(self.ordered_words) == other

        return False

    def __getitem__(self, index):
        return self.ordered_words[index]

    def __len__(self):
        return len(self.ordered_words)

    def __iter__(self):
        for word in self.ordered_words:
            yield word

    def discard(self, other):
        try:
            self.ordered_words.remove(other)
        except ValueError:
            pass

class OrderedSetTests(unittest.TestCase):

    """Tests for OrderedSet."""

    def test_constructor(self):
        OrderedSet([1, 2, 3, 4])

    def test_iterable(self):
        numbers = OrderedSet([1, 2, 3, 4])
        self.assertEqual(set(numbers), {1, 2, 3, 4})

    def test_uniqueness(self):
        numbers = OrderedSet([1, 3, 2, 4, 2, 1, 4, 5])
        self.assertEqual(sorted(numbers), [1, 2, 3, 4, 5])

    def test_maintains_order_and_uniqueness(self):
        string = "Hello world.  This string contains many characters in it."
        expected = "Helo wrd.Thistngcamy"
        characters = OrderedSet(string)
        self.assertEqual("".join(characters), expected)

    def test_length(self):
        numbers = OrderedSet([1, 2, 4, 2, 1, 4, 5])
        self.assertEqual(len(numbers), 4)
        self.assertEqual(len(OrderedSet('hiya')), 4)
        self.assertEqual(len(OrderedSet('hello there')), 7)

    def test_containment(self):
        numbers = OrderedSet([1, 2, 4, 2, 1, 4, 5])
        self.assertIn(2, numbers)
        self.assertNotIn(3, numbers)

    def test_memory_and_time_efficient(self):
        # Time efficient construction
        same = [9999 for _ in range(5000)]
        different = [9999 + i for i in range(5000)]
        time = partial(
            timer,
            globals={**globals(), "same": same, "different": different},
        )
        small_set_time = time("OrderedSet(same)", number=10)
        large_set_time = time("OrderedSet(different)", number=10)
        self.assertGreater(small_set_time*50, large_set_time)

        # Memory efficient
        numbers = OrderedSet([9999 for _ in range(10_000)])
        numbers2 = OrderedSet([9999 + i for i in range(10_000)])
        self.assertLess(get_size(numbers)*10, get_size(numbers2))
        self.assertLess(get_size(numbers), 12_000)

        # Time efficient lookups
        first = next(iter(numbers2))
        last = next(islice(numbers2, 9999))
        time = partial(timer, globals=locals(), number=10)
        beginning_lookup = time("assert first in numbers2")
        end_lookup = time("assert last in numbers2")
        not_in_lookup = time("assert 20_000 not in numbers2")
        self.assertGreater(beginning_lookup*20, end_lookup)
        self.assertGreater(end_lookup*20, beginning_lookup)
        self.assertGreater(beginning_lookup*20, not_in_lookup)
        self.assertGreater(end_lookup*20, not_in_lookup)
        self.assertGreater(not_in_lookup*20, end_lookup)
        self.assertGreater(not_in_lookup*20, beginning_lookup)

    # Bonus 1
    # @unittest.expectedFailure
    def test_add_and_discard(self):
        numbers = OrderedSet([1, 2, 3])
        numbers.add(3)
        self.assertEqual(len(numbers), 3)
        numbers.add(4)
        self.assertEqual(len(numbers), 4)
        numbers.discard(4)
        self.assertEqual(len(numbers), 3)
        numbers.discard(4)
        self.assertEqual(len(numbers), 3)

        # Check for add method efficiency
        setup = "numbers = OrderedSet([])"
        time = partial(timer, setup=setup, globals=globals(), number=100)
        small_set_time = time(dedent("""
            add = numbers.add
            for n in [9999 for _ in range(700)]:
                add(n)
        """))
        large_set_time = time(dedent("""
            add = numbers.add
            for n in [9999 + i for i in range(700)]:
                add(n)
        """))
        self.assertGreater(small_set_time*50, large_set_time)

    # Bonus 2
    # @unittest.expected    # # Bonus 3
    # # @unittest.expectedFailure
    # def test_supports_indexing(self):
    #     string = "Hello world.  This string contains many characters in it."
    #     characters = OrderedSet(string)
    #     self.assertEqual(characters[0], 'H')
    #     self.assertEqual(characters[2], 'l')
    #     self.assertEqual(characters[3], 'o')
    #     self.assertEqual(characters[-1], 'y')Failure
    def test_equality(self):
        self.assertEqual(OrderedSet('abc'), OrderedSet('abc'))
        self.assertNotEqual(OrderedSet('abc'), OrderedSet('bac'))
        self.assertEqual(OrderedSet('abc'), set('abc'))
        self.assertEqual(OrderedSet('bac'), set('abc'))
        self.assertNotEqual(OrderedSet('abc'), 'abc')
        self.assertNotEqual(OrderedSet('abc'), ['a', 'b', 'c'])
        numbers = OrderedSet([1, 2, 3])
        numbers2 = OrderedSet([1, 2, 3, 4])
        self.assertNotEqual(numbers, numbers2)
        self.assertFalse(numbers == numbers2)
        numbers.add(4)
        self.assertEqual(numbers, numbers2)
        self.assertFalse(numbers != numbers2)

    # Bonus 3
    # @unittest.expectedFailure
    def test_supports_indexing(self):
        string = "Hello world.  This string contains many characters in it."
        characters = OrderedSet(string)
        self.assertEqual(characters[0], 'H')
        self.assertEqual(characters[2], 'l')
        self.assertEqual(characters[3], 'o')
        self.assertEqual(characters[-1], 'y')


def auto_time(code, *, setup="", globals, repeat=7, number=1, threshold=10000):
    """
    Return the time the given code takes to run.

    Runs code until total time is greater than the threshold (in nanoseconds).

    Times code with increasing numbers from the sequence 1, 2, 5, 10, 20, 50,
    etc. Code is run repeatedly each time, taking the minimum time per run.
    """
    timer = timeit.Timer(code, setup, perf_counter_ns, globals)
    time_taken = min(timer.repeat(repeat, number))
    while time_taken < threshold:
        number *= 2
        time_taken = min(timer.repeat(repeat, number))
    return time_taken/number


def timer(code, globals, number, setup=""):
    return auto_time(
        code,
        number=number,
        globals=globals,
        setup=setup,
        threshold=5000,
    )


def get_size(obj, seen=None):
    """Return size of any Python object."""
    if seen is None:
        seen = set()
    size = getsizeof(obj)
    if id(obj) in seen:
        return 0
    seen.add(id(obj))
    if hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    if hasattr(obj, '__slots__'):
        size += sum(
            get_size(getattr(obj, attr), seen)
            for attr in obj.__slots__
            if hasattr(obj, attr)
        )
    if isinstance(obj, Mapping):
        size += sum(
            get_size(k, seen) + get_size(v, seen)
            for k, v in obj.items()
        )
    elif isinstance(obj, Iterable) and not isinstance(obj, (str, bytes)):
        size += sum(get_size(item, seen) for item in obj)
    return size


class ColorTestResult(unittest.TextTestResult):
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln(f"{self.GREEN}OK{self.RESET}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.writeln(f"{self.RED}FAIL{self.RESET}")

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.writeln(f"{self.RED}ERROR{self.RESET}")

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self.stream.writeln(f"{self.YELLOW}UNEXPECTED SUCCESS{self.RESET}")


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    class resultclass(ColorTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=AllowUnexpectedSuccessRunner,
    )
