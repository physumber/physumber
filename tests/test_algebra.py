import unittest
from physumber.sumbermath.algebra import algebra

class TestAlgebra(unittest.TestCase):
    def test_modulus(self):
        alg = algebra()
        self.assertEqual(alg.modulus(-5), 5)
        self.assertEqual(alg.modulus(10), 10)
        self.assertEqual(alg.modulus(0), 0)
        self.assertEqual(alg.modulus(-3.7), 3.7)

if __name__ == "__main__":
    unittest.main()
