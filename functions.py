import numpy as np
import math

def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    res = 1
    for i in range(min(len(x), len(x[0]))):
        if (x[i][i] != 0):
            res *= int(x[i][i])
    return res
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    xp = []
    yp = []
    for val in x:
        xp.append(val)
    for val in y:
        yp.append(val)
    xp.sort()
    yp.sort()
    return xp == yp
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    mx = 0
    n = len(x)
    for i in range(n):
        if (i - 1 >= 0 and x[i - 1] == 0):
            mx = max(mx, x[i])
    return mx
    pass


def convert_image(orig, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    h = len(orig)
    w = len(orig[0])
    img = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            for k in range(3):
                img[i][j] += orig[i][j][k] * coefs[k]
    return img
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    elements = []
    counters = []
    for i in range(len(x)):
        if (i == 0 or x[i] != x[i - 1]):
            elements.append(x[i])
            counters.append(1)
        else:
            counters[-1] += 1
    return elements, counters
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    n = len(x)
    m = len(y)
    dist = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(len(x[i])):
                s += (x[i][k] - y[j][k]) ** 2
            dist[i][j] = math.sqrt(s)
    return dist
    pass
