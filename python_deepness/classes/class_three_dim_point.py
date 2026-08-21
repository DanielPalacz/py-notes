from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int

    def __eq__(self, other):

        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True

        return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other_scalar):
        return Point(self.x * other_scalar, self.y * other_scalar, self.z * other_scalar)

    def __rmul__(self, other_scalar):
        return Point(self.x * other_scalar, self.y * other_scalar, self.z * other_scalar)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

########################################################################################################################

import unittest


class PointTests(unittest.TestCase):

    """Tests for Point."""

    def test_attributes(self):
        point = Point(1, 2, 3)
        self.assertEqual((point.x, point.y, point.z), (1, 2, 3))
        point.x = 4
        self.assertEqual(point.x, 4)

    def test_string_representation(self):
        point = Point(1, 2, 3)
        self.assertEqual(str(point), 'Point(x=1, y=2, z=3)')
        self.assertEqual(repr(point), 'Point(x=1, y=2, z=3)')
        point.y = 4
        self.assertEqual(str(point), 'Point(x=1, y=4, z=3)')
        self.assertEqual(repr(point), 'Point(x=1, y=4, z=3)')

    def test_equality_and_inequality(self):
        p1 = Point(1, 2, 3)
        p2 = Point(1, 2, 4)
        p3 = Point(1, 2, 3)
        self.assertNotEqual(Point(1, 2, 3), Point(1, 2, 4))
        self.assertEqual(Point(1, 2, 3), Point(1, 2, 3))
        self.assertFalse(Point(1, 2, 3) != Point(1, 2, 3))
        self.assertNotEqual(p1, p2)
        self.assertEqual(p1, p3)
        p3.x, p3.z = p3.z, p3.x
        self.assertNotEqual(p1, p3)
        self.assertTrue(p1 != p3)
        self.assertFalse(p1 == p3)

    # Bonus 1
    # @unittest.expectedFailure
    def test_shifting(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        p3 = p2 + p1
        p4 = p3 - p1
        self.assertEqual((p3.x, p3.y, p3.z), (5, 7, 9))
        self.assertEqual((p4.x, p4.y, p4.z), (p2.x, p2.y, p2.z))

    # Bonus 2
    # @unittest.expectedFailure
    def test_scale(self):
        p1 = Point(1, 2, 3)
        p2 = p1 * 2
        self.assertEqual((p2.x, p2.y, p2.z), (2, 4, 6))
        p3 = 3 * p1
        self.assertEqual((p3.x, p3.y, p3.z), (3, 6, 9))

    # Bonus 3
    # @unittest.expectedFailure
    def test_iterable_point(self):
        point = Point(x=1, y=2, z=3)
        x, y, z = point
        self.assertEqual((x, y, z), (1, 2, 3))


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":

    try:
        unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
    except SystemExit:
        pass
