import numpy as np


def create_companion_matrix(coefficients):
    # TODO: Check if input is valid and check if leading coefficient is zero

    n = coefficients.size-1
    c = np.flip(coefficients, 0)
    mat = np.eye(n, k=-1)
    mat[:, n-1] = -c[:n]
    return mat
