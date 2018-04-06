from unittest import TestCase


class TestCreate_gershgorin_discs(TestCase):
    def test_vector_input(self):
        import numpy as np
        from GershgorinDisc import create_gershgorin_discs
        vec = np.matrix('1, 1, 1')
        self.assertFalse(create_gershgorin_discs(vec))

    def test_non_square_matrix_input(self):
        import numpy as np
        from GershgorinDisc import create_gershgorin_discs
        A = np.matrix('1, 1, 1; 1, 1, 1')
        create_gershgorin_discs(A)
