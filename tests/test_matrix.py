import unittest
from apex_matrix.matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_addition(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[5, 6], [7, 8]])
        result = matrix_a + matrix_b
        expected = Matrix([[6, 8], [10, 12]])
        self.assertEqual(result, expected)

    def test_matrix_x_matrix_multiplication(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[5, 6, 7], [8, 9 , 10]])
        result = matrix_a * matrix_b
        expected = Matrix([[21, 24, 27], [47, 54, 61]])
        self.assertEqual(result, expected)

    def test_matrix_x_scalar_multiplication(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        result = matrix_a * 2
        expected = Matrix([[2, 4], [6, 8]])
        self.assertEqual(result, expected)

    def test_scalar_x_matrix_multiplication(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        result = 2 * matrix_a
        expected = Matrix([[2, 4], [6, 8]])
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()