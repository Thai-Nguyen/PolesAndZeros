from unittest import TestCase


class TestCreateCompanionMatrix(TestCase):
    def test_odd_leading_coefficient(self):
        # Testing case where the given polynomial is
        # x^3 + 3x^2 + 4x + 5
        import numpy as np
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 3, 4, 5))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, 0, -5; 1, 0, -4; 0, 1, -3')
        self.assertEqual(test_mat, true_mat)

    def test_even_leading_coefficient(self):
        # Testing case where the given polynomial is
        # x^4 + 5x^3 + 4x^2 + 2x + 1
        import numpy as np
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 5, 4, 2, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = np.matrix('0, 0, 0, -1; 1, 0, 0, -2; 0, 1, 0, -4; 0, 0, 0, -5')
        self.assertEqual(test_mat, true_mat)

    def test_one_zero_coefficient(self):
        # Testing case where the given polynomial is
        # x^2 + 0x + 1
        import numpy as np
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((1, 0, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = 1  #TODO: Make companion matrix for polynomial x^2 + 1
        self.assertEqual(test_mat, true_mat)

    def test_leading_coefficient_zero(self):
        # Testing case where the given polynomial is
        # 0x^2 + x + 1
        import numpy as np
        from CompanionMatrix import create_companion_matrix
        coeffs = np.array((0, 1, 1))
        test_mat = create_companion_matrix(coeffs)
        true_mat = 1  # TODO: Make companion matrix for polynomial x + 1
        self.assertEqual(test_mat, true_mat)
