import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection


def create_gershgorin_discs(mat):
    if mat.shape[0] != mat.shape[1]:
        print('Error: Input must be a square matrix')
        return False

    n = len(mat)

    x = np.zeros(n)
    y = np.zeros(n)
    r = np.zeros(n)
    for i in range(n):
        x[i] = np.real(mat[(i, i)])
        y[i] = np.imag(mat[(i, i)])
        r[i] = np.sum(np.abs(mat[i, :])) - np.abs(mat[i, i])

    return x, y, r


def plot_gershgorin_discs(x, y, r):
    # TODO: Check if x, y, r vectors are valid (all same length, contains complex numbers)

    # Draw discs
    n = x.size
    patches = []
    for i in range(n):
        circle = Circle((x[i], y[i]), r[i])
        patches.append(circle)

    # Plot
    fig, ax = plt.subplots()
    p = PatchCollection(patches, alpha=0.2)
    ax.add_collection(p)
    plt.axis('equal')

    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # Sample plot of a given matrix A
    A = np.matrix('10, -1, 0, 1; 0.2, 8 0.2, 0.2; 1, 1, 2, 1; -1, -1, -1, -11')
    x, y, r = create_gershgorin_discs(A)
    plot_gershgorin_discs(x, y, r)
