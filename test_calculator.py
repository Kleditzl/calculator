#hello there
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(3,4), 7)
    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(4, 1), 3)
    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(2,3), 6)
    def test_division(self):
        self.assertEqual(calculator.division(4, 1), 4)
        self.assertEqual(calculator.division(4, 0), 0)
        self.assertEqual(calculator.division(0, 4), 0)
        self.assertEqual(calculator.division(2,6), (1/3))

if __name__ == '__main__':
    unittest.main()
