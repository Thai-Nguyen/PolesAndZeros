from unittest import TestCase
import numpy as np


class TestCreateCompanionMatrix(TestCase):
    def test_odd_leading_coefficient(self):
        # Testing case where the given polynomial is
        # x^3 + 3x^2 + 4x + 5
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 3, 4, 5))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, 0, -5; 1, 0, -4; 0, 1, -3')
        np.testing.assert_array_equal(test_mat, true_mat)

    def test_even_leading_coefficient(self):
        # Testing case where the given polynomial is
        # x^4 + 5x^3 + 4x^2 + 2x + 1
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 5, 4, 2, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, 0, 0, -1; 1, 0, 0, -2; 0, 1, 0, -4; 0, 0, 1, -5')
        np.testing.assert_array_equal(test_mat, true_mat)

    def test_one_zero_coefficient(self):
        # Testing case where the given polynomial is
        # x^2 + 0x + 1
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 0, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, -1; 1, 0')
        np.testing.assert_array_equal(test_mat, true_mat)

    def test_leading_coefficient_zero(self):
        # Testing case where the given polynomial is
        # 0x^2 + x + 1
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((0, 1, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('-1')
        np.testing.assert_array_equal(test_mat, true_mat)

    def test_zero_constant_term(self):
        # Testing case where the given polynomial is
        # x^2 + x + 0
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 1, 0))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, 0; 1, -1')
        np.testing.assert_array_equal(test_mat, true_mat)

    def test_non_monic_polynomial(self):
        # Testing case where the given polynomial is
        # 4x^3 + 2x^2 + x + 1
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((4, 2, 1, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, 0, -0.25; 1, 0, -0.25; 0, 1, -0.5')
        np.testing.assert_array_almost_equal(test_mat, true_mat)
