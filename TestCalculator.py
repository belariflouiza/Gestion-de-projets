from Calculator import sum,mult,div
import unittest

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        
        self.assertEqual(sum(3, 5), 8)


    def test_mult(self):
        self.assertEqual(mult(3, 5), 15)
  

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        with self.assertRaises(ValueError):
            div(10, 0)


if __name__ == '__main__':
    unittest.main()