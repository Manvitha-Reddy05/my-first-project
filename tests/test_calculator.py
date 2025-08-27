import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calculator.sub(10, 4), 6)

    def test_mul(self):
        self.assertEqual(calculator.mul(3, 5), 15)

    def test_div_normal(self):
        self.assertEqual(calculator.div(10, 2), 5)

    def test_div_by_zero(self):
        self.assertEqual(calculator.div(8, 0), "Cannot divide by zero")

if __name__ == "__main__":
    unittest.main()
