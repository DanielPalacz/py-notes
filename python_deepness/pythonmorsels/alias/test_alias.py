import unittest


from alias import alias


class AliasTests(unittest.TestCase):

    """Tests for alias."""

    def test_mirrors_attribute_on_class(self):
        class Thing:
            one = 4
            two = alias('one')
        thing = Thing()
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)

    def test_mirrors_attribute_from_initializer(self):
        class Thing:
            two = alias('one')
            def __init__(self):
                self.one = 4
        thing = Thing()
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)

    def test_attribute_mirroring_maintained(self):
        class Thing:
            one = 4
            two = alias('one')
        thing = Thing()
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)
        thing.one = 6
        self.assertEqual(thing.one, 6)
        self.assertEqual(thing.two, 6)
        self.assertNotEqual(thing.two, 4)

    def test_attribute_identity(self):
        class Thing:
            two = alias('one')
            def __init__(self, one):
                self.one = one
        my_list = []
        thing = Thing(my_list)
        self.assertIs(thing.one, thing.two, my_list)

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_attribute_unwritable_by_default(self):
        class Thing:
            one = 4
            two = alias('one')
        thing = Thing()
        with self.assertRaises(AttributeError):
            thing.two = 6
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)

    # To test bonus 2, comment out the next line
    @unittest.expectedFailure
    def test_writable_attribute(self):
        class Thing2:
            blue = alias('red', write=True)
            red = []
        thing2 = Thing2()
        self.assertIs(thing2.blue, thing2.red)
        thing2.blue = [4, 5]
        self.assertEqual(thing2.blue, [4, 5])
        self.assertIs(thing2.blue, thing2.red)

        # write=False raises an AttributeError (mutation works though)
        class Thing3:
            blue = alias('red', write=False)
            red = []
        thing3 = Thing3()
        with self.assertRaises(AttributeError):
            thing3.blue = [4, 5]
        thing3.blue.append(6)
        self.assertEqual(thing3.blue, [6])
        self.assertIs(thing3.blue, thing3.red)

    # To test bonus 3, comment out the next line
    @unittest.expectedFailure
    def test_attribute_mirrored_on_class(self):
        class Thing:
            one = 4
            two = alias('one')
        self.assertEqual(Thing.one, 4)
        self.assertEqual(Thing.two, 4)


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
