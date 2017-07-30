# Matrix multiplicator
# By Niels Wadsholt, October 2015

def matrix_multi(m1, m2):
    """
    Multiplies two matrices represented as lists of lists.
    """
    
    assert len(m1[0]) == len(m2), "ERROR: Number of m1 columns must match m2 rows"
    
    return [[sum([m1[h][i] * m2[i][j] for i in range(len(m2))])
             for j in range(len(m2[0]))] for h in range(len(m1))]


def m_print(m):
    """
    Pretty-prints a lists of lists matrix
    """
    
    for row in range(len(m)):
        for item in m[row]:
            print item, "\t",
        print
    print


# =================================== Test ===================================

def test():
    # a1 = [[1, 2, 3],
          # [4, 5, 6]]

    # b1 = [[7, 8],
          # [9, 10],
          # [11, 12]]

    # a2 = [[3, 4, 2]]

    # b2 = [[13, 9, 7, 15],
          # [8, 7, 4, 6],
          # [6, 4, 0, 3]]

    # a3 = [[0, 2, 2],
          # [0, 1, 3]]

    # b3 = [[2, 1],
          # [2, 0],
          # [2, 0]]

    # a4 = [[0, 1, 2],
          # [3, 4, 5],
          # [6, 7, 8]]

    # m_print(matrix_multi(a1, b1))
    # m_print(matrix_multi(a2, b2))

    # m_print(matrix_multi(a3, b3))
    # m_print(matrix_multi(b3, a3))

    # m_print(matrix_multi(a4, a4))


    # Matrix multiplication can also be done with numpy's .dot:
    # import numpy as np

    # print np.dot(a3, b3)
    # print np.dot(b3, a3)
    # print

    # Note: Instead of lists, it is recommended to use numpy arrays:
    # np_a3 = np.array(a3)
    # np_b3 = np.array(b3)
    # print np.dot(np_a3, np_b3)
    # print np.dot(np_b3, np_a3)
    # print


    # ========== Multiplying adjacency matrices ===========
    # a1 = [[0, 1, 1, 0],
          # [1, 0, 0, 1],
          # [1, 0, 0, 1],
          # [0, 1, 1, 0]]

    # a1 = [[0, 0, 1],
          # [0, 0, 1],
          # [1, 1, 0]]

    a1 = [[0, 0, 1, 0],
          [0, 0, 1, 1],
          [1, 1, 0, 1],
          [0, 1, 1, 0]]

    # a1 = [[0, 0, 1, 0],
          # [0, 0, 0, 1],
          # [1, 0, 0, 1],
          # [0, 1, 1, 0]]

    a2 = matrix_multi(a1, a1) # a**2
    a3 = matrix_multi(a2, a1) # a**3
    a4 = matrix_multi(a3, a1) # a**4
    a5 = matrix_multi(a4, a1) # a**5

    m_print(a1)
    m_print(a2)
    m_print(a3)
    m_print(a4)
    m_print(a5)

# test()