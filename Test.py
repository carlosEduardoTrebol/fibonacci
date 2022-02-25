#CARLOS
import unittest
import fibonacci

class FibonacciShould(unittest.TestCase):

    def test_returns_cero_when_is_first_case(self):
        fibo = fibonacci.fibonacci()
        number = fibo.run_secuence_fibonacci()
        self.assertEqual(number, "0")