'''
Matrix multiplicator

Copyright (C) 2015 Niels Wadsholt
'''

def matrix_multi(m1, m2):
    """
    Multiplies two matrices represented as lists of lists.
    """
    
    assert len(m1[0]) == len(m2), "ERROR: Number of m1 columns must match m2 rows"
    
    return [[sum([m1[h][i] * m2[i][j] for i in range(len(m2))])
             for j in range(len(m2[0]))] for h in range(len(m1))]


def m_print(m):
    """
    Pretty-prints a list-of-lists matrix.
    """
    
    for row in range(len(m)):
        for item in m[row]:
            print item, "\t",
        print
    print

