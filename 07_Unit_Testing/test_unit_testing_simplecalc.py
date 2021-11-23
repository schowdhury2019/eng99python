from simple_calc import SimpleCalc
import unittest

class SimpleCalcTest(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalc()

    def tearDown(self):
        # remove newly generated files, database connections
        # last thing that gets executed
        pass

    def test_add(self):
        actual = self.calc.add(2,4)
        expected = 6
        self.assertEqual(expected, actual)

    def test_subtract(self):
        actual = self.calc.subtract(15,5)
        expected = (15-5)
        self.assertEqual(expected,actual)

    def test_mult(self):
        actual = self.calc.mult(2,5)
        expected = (2*5)
        self.assertEqual(expected,actual)

    def test_divide(self):
        actual = self.calc.divide(15,5)
        expected = (15/5)
        self.assertEqual(expected,actual)

    def test_mult_floats(self):
        self.assertAlmostEqual(7.85, self.calc.mult(3.14,2.5))

if __name__ == "__main__":
    unittest.main()