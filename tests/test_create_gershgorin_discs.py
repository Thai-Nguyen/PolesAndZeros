from unittest import TestCase


class TestCreateGershgorinDiscs(TestCase):
    def test_vector_input(self):
        import numpy as np
        from GershgorinDisc import create_gershgorin_discs
        vec = np.array([[1, 1, 1]])
        self.assertFalse(create_gershgorin_discs(vec))

    def test_non_square_matrix_input(self):
        import numpy as np
        from GershgorinDisc import create_gershgorin_discs
        mat = np.array([[1, 1, 1], [1, 1, 1]])
        self.assertFalse(create_gershgorin_discs(mat))

    def test_empty_matrix(self):
        import numpy as np
        from GershgorinDisc import create_gershgorin_discs
        mat = np.array([[]])
        self.assertFalse(create_gershgorin_discs(mat))

    def test_scalar_input(self):
        import numpy as np
        from GershgorinDisc import create_gershgorin_discs
        mat = np.array([[1]])
        self.assertFalse(create_gershgorin_discs(mat))
