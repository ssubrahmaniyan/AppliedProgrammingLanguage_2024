import unittest
from matmul_correct import matrix_multiply

class TestMatrixMultiplication(unittest.TestCase):

    def test_square_matrices(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_rectangular_matrices(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        result = [[58, 64], [139, 154]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_multiply_with_identity_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        identity_matrix = [[1, 0], [0, 1]]
        result = [[1, 2], [3, 4]]
        self.assertEqual(matrix_multiply(matrix1, identity_matrix), result)

    def test_non_square_result(self):
        matrix1 = [[1, 2, 3]]
        matrix2 = [[4], [5], [6]]
        result = [[32]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_mismatched_dimensions(self):
        matrix1 = [[1, 2]]
        matrix2 = [[3, 4], [5, 6], [7, 8]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_non_numeric_elements(self):
        matrix1 = [[1, 2], [3, 'a']]
        matrix2 = [[4, 5], [6, 7]]
        with self.assertRaises(TypeError):
            matrix_multiply(matrix1, matrix2)

    def test_empty_matrix(self):
        matrix1 = []
        matrix2 = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_non_uniform_rows(self):
        matrix1 = [[1, 2, 3], [4, 5]]
        matrix2 = [[6, 7], [8, 9], [10, 11]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_single_element_matrices(self):
        matrix1 = [[2]]
        matrix2 = [[3]]
        result = [[6]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_matrix_with_zero_elements(self):
        matrix1 = [[0, 0], [0, 0]]
        matrix2 = [[0, 0], [0, 0]]
        result = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_non_square_identity_matrix(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(matrix_multiply(matrix1, identity_matrix), result)

    def test_matrix_with_negative_elements(self):
        matrix1 = [[-1, -2], [-3, -4]]
        matrix2 = [[1, 2], [3, 4]]
        result = [[-7, -10], [-15, -22]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_matrix_with_fractional_elements(self):
        matrix1 = [[0.5, 1.5], [2.5, 3.5]]
        matrix2 = [[4.5, 5.5], [6.5, 7.5]]
        result = [[12.0, 14.0], [34.0, 40.0]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_multiply_by_zero_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        zero_matrix = [[0, 0], [0, 0]]
        result = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiply(matrix1, zero_matrix), result)

    def test_symmetric_matrix_multiplication(self):
        matrix1 = [[2, 3], [3, 4]]
        result = [[13, 18], [18, 25]]
        self.assertEqual(matrix_multiply(matrix1, matrix1), result)

    def test_matrix_with_large_numbers(self):
        matrix1 = [[10**10, 2 * 10**10], [3 * 10**10, 4 * 10**10]]
        matrix2 = [[10**10, 2 * 10**10], [3 * 10**10, 4 * 10**10]]
        result = [[7 * 10**20, 10 * 10**20], [15 * 10**20, 22 * 10**20]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_matrix_of_ones(self):
        matrix1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        matrix2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        result = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_empty_matrices(self):
        matrix1 = []
        matrix2 = []
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_single_element_complex_matrices(self):
        matrix1 = [[complex(1, 1)]]
        matrix2 = [[complex(2, 2)]]
        result = [[complex(0, 4)]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_non_conformable_matrices(self):
        matrix1 = [[complex(1, 1), complex(2, 2)]]
        matrix2 = [[complex(3, 3)]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_identity_matrix_with_complex(self):
        matrix1 = [[complex(1, 2), complex(3, 4)], [complex(5, 6), complex(7, 8)]]
        identity_matrix = [[complex(1, 0), complex(0, 0)], [complex(0, 0), complex(1, 0)]]
        result = [[complex(1, 2), complex(3, 4)], [complex(5, 6), complex(7, 8)]]
        self.assertEqual(matrix_multiply(matrix1, identity_matrix), result)

    def test_large_matrices_with_complex_numbers(self):
        matrix1 = [[complex(i, i) for i in range(10)] for _ in range(10)]
        matrix2 = [[complex(i, -i) for i in range(10)] for _ in range(10)]
        
        # Correctly compute the expected result matrix
        result = []
        for r in range(10):
            row = []
            for c in range(10):
                sum_real = 0
                sum_imag = 0
                for k in range(10):
                    a = matrix1[r][k]
                    b = matrix2[k][c]
                    product = a * b
                    sum_real += product.real
                    sum_imag += product.imag
                row.append(complex(sum_real, sum_imag))
            result.append(row)
        
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_matrix_with_only_imaginary_numbers(self):
        matrix1 = [[complex(0, 1), complex(0, 2)], [complex(0, 3), complex(0, 4)]]
        matrix2 = [[complex(0, 5), complex(0, 6)], [complex(0, 7), complex(0, 8)]] 
        result = [[complex(-19, 0), complex(-22, 0)], [complex(-43, 0), complex(-50, 0)]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

    def test_matrix_with_zero_elements(self):
        matrix1 = [[complex(0, 0), complex(0, 0)], [complex(0, 0), complex(0, 0)]]
        matrix2 = [[complex(0, 0), complex(0, 0)], [complex(0, 0), complex(0, 0)]]
        result = [[complex(0, 0), complex(0, 0)], [complex(0, 0), complex(0, 0)]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), result)

if __name__ == '__main__':
    unittest.main()
