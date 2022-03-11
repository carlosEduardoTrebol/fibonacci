#CARLOS
import unittest
import fibonacci

class FibonacciShould(unittest.TestCase):

    def test_returns_cero_when_is_first_case(self):
        fibo = fibonacci.fibonacci()
        number = fibo.run_secuence_fibonacci(0)
        self.assertEqual(number, "0")

    def test_returns_two_when_is_second_case(self):
        fibo = fibonacci.fibonacci()
        number = fibo.run_secuence_fibonacci(1)
        self.assertEqual(number, "1")

    def test_ReturnNumberFromPosition(self):
        fibo = fibonacci.fibonacci()
        number = fibo.run_secuence_fibonacci(15)
        self.assertEqual(number, "610")

    # def test_returns_three_when_is_third_case(self):
    #     fibo = fibonacci.fibonacci()
    #     number = fibo.run_secuence_fibonacci(2)
    #     self.assertEqual(number, "1")