from base_converter import *
from combi_plot import *
from matrix_multi import *
from time_func import *
from what_you_give import *


def base_converter_test():
    print "dec_to_bin(42)\t-->\t", dec_to_bin(42)
    print "bin_to_dec(101010)\t-->\t", bin_to_dec(101010)
    print

    print "bin_to_dec(dec_to_bin(7))\t-->\t", bin_to_dec(dec_to_bin(7))
    print "dec_to_bin(bin_to_dec(111))\t-->\t", dec_to_bin(bin_to_dec(111))
    print

    print "bin_to_dec(0)\t-->\t", bin_to_dec(0)
    print "bin_to_dec(1)\t-->\t", bin_to_dec(1)
    print "bin_to_dec(10)\t-->\t", bin_to_dec(10)
    print "bin_to_dec(11)\t-->\t", bin_to_dec(11)
    print "bin_to_dec(100)\t-->\t", bin_to_dec(100)
    print "bin_to_dec(101)\t-->\t", bin_to_dec(101)
    print "bin_to_dec(110)\t-->\t", bin_to_dec(110)
    print "bin_to_dec(111)\t-->\t", bin_to_dec(111)
    print "bin_to_dec(1000)\t-->\t", bin_to_dec(1000)
    print "bin_to_dec(1001)\t-->\t", bin_to_dec(1001)
    print "bin_to_dec(1010)\t-->\t", bin_to_dec(1010)
    print "bin_to_dec(1011)\t-->\t", bin_to_dec(1011)
    print "bin_to_dec(1100)\t-->\t", bin_to_dec(1100)
    print "bin_to_dec(1101)\t-->\t", bin_to_dec(1101)
    print "bin_to_dec(1110)\t-->\t", bin_to_dec(1110)
    print "bin_to_dec(1111)\t-->\t", bin_to_dec(1111)
    print

    print "dec_to_bin(0)\t-->\t", dec_to_bin(0)
    print "dec_to_bin(1)\t-->\t", dec_to_bin(1)
    print "dec_to_bin(2)\t-->\t", dec_to_bin(2)
    print "dec_to_bin(3)\t-->\t", dec_to_bin(3)
    print "dec_to_bin(4)\t-->\t", dec_to_bin(4)
    print "dec_to_bin(5)\t-->\t", dec_to_bin(5)
    print "dec_to_bin(6)\t-->\t", dec_to_bin(6)
    print "dec_to_bin(7)\t-->\t", dec_to_bin(7)
    print "dec_to_bin(8)\t-->\t", dec_to_bin(8)
    print "dec_to_bin(9)\t-->\t", dec_to_bin(9)
    print "dec_to_bin(10)\t-->\t", dec_to_bin(10)
    print "dec_to_bin(11)\t-->\t", dec_to_bin(11)
    print "dec_to_bin(12)\t-->\t", dec_to_bin(12)
    print "dec_to_bin(13)\t-->\t", dec_to_bin(13)
    print "dec_to_bin(14)\t-->\t", dec_to_bin(14)
    print "dec_to_bin(15)\t-->\t", dec_to_bin(15)
    print

    print "convert(42, 10, 2)\t-->\t", convert(42, 10, 2)
    print "convert(42, 10, 3)\t-->\t", convert(42, 10, 3)
    print "convert(42, 10, 4)\t-->\t", convert(42, 10, 4)
    print "convert(42, 10, 5)\t-->\t", convert(42, 10, 5)
    print "convert(42, 10, 6)\t-->\t", convert(42, 10, 6)
    print "convert(42, 10, 7)\t-->\t", convert(42, 10, 7)
    print "convert(42, 10, 8)\t-->\t", convert(42, 10, 8)
    print "convert(42, 10, 9)\t-->\t", convert(42, 10, 9)
    print "convert(42, 10, 10)\t-->\t", convert(42, 10, 10)
    print

    print "convert(101010, 2, 10)\t-->\t", convert(101010, 2, 10)
    print "convert(1120, 3, 10)\t-->\t", convert(1120, 3, 10)
    print "convert(222, 4, 10)\t-->\t", convert(222, 4, 10)
    print "convert(132, 5, 10)\t-->\t", convert(132, 5, 10)
    print "convert(110, 6, 10)\t-->\t", convert(110, 6, 10)
    print "convert(60, 7, 10)\t-->\t", convert(60, 7, 10)
    print "convert(52, 8, 10)\t-->\t", convert(52, 8, 10)
    print "convert(46, 9, 10)\t-->\t", convert(46, 9, 10)
    print "convert(42, 10, 10)\t-->\t", convert(42, 10, 10)
    print

    print "convert(101010, 2, 2)\t-->\t", convert(101010, 2, 2)
    print "convert(101010, 2, 3)\t-->\t", convert(101010, 2, 3)
    print "convert(101010, 2, 4)\t-->\t", convert(101010, 2, 4)
    print "convert(101010, 2, 5)\t-->\t", convert(101010, 2, 5)
    print "convert(101010, 2, 6)\t-->\t", convert(101010, 2, 6)
    print "convert(101010, 2, 7)\t-->\t", convert(101010, 2, 7)
    print "convert(101010, 2, 8)\t-->\t", convert(101010, 2, 8)
    print "convert(101010, 2, 9)\t-->\t", convert(101010, 2, 9)
    print "convert(101010, 2, 10)\t-->\t", convert(101010, 2, 10)
    print

    print "convert(52, 8, 2)\t-->\t", convert(52, 8, 2)
    print "convert(52, 8, 3)\t-->\t", convert(52, 8, 3)
    print "convert(52, 8, 4)\t-->\t", convert(52, 8, 4)
    print "convert(52, 8, 5)\t-->\t", convert(52, 8, 5)
    print "convert(52, 8, 6)\t-->\t", convert(52, 8, 6)
    print "convert(52, 8, 7)\t-->\t", convert(52, 8, 7)
    print "convert(52, 8, 8)\t-->\t", convert(52, 8, 8)
    print "convert(52, 8, 9)\t-->\t", convert(52, 8, 9)
    print "convert(52, 8, 10)\t-->\t", convert(52, 8, 10)
    print

    print "convert(-52, 8, 2)\t-->\t", convert(-52, 8, 2)
    print "convert(-52, 8, 3)\t-->\t", convert(-52, 8, 3)
    print "convert(-52, 8, 4)\t-->\t", convert(-52, 8, 4)
    print "convert(-52, 8, 5)\t-->\t", convert(-52, 8, 5)
    print "convert(-52, 8, 6)\t-->\t", convert(-52, 8, 6)
    print "convert(-52, 8, 7)\t-->\t", convert(-52, 8, 7)
    print "convert(-52, 8, 8)\t-->\t", convert(-52, 8, 8)
    print "convert(-52, 8, 9)\t-->\t", convert(-52, 8, 9)
    print "convert(-52, 8, 10)\t-->\t", convert(-52, 8, 10)
    print
    
    print "convert(convert(1120, 3, 2), 2, 3)\t-->\t", convert(convert(1120, 3, 2), 2, 3)
    print "convert(convert(1120, 3, 4), 4, 3)\t-->\t", convert(convert(1120, 3, 4), 4, 3)
    print "convert(convert(1120, 3, 5), 5, 3)\t-->\t", convert(convert(1120, 3, 5), 5, 3)
    print "convert(convert(1120, 3, 6), 6, 3)\t-->\t", convert(convert(1120, 3, 6), 6, 3)
    print "convert(convert(1120, 3, 7), 7, 3)\t-->\t", convert(convert(1120, 3, 7), 7, 3)
    print "convert(convert(1120, 3, 8), 8, 3)\t-->\t", convert(convert(1120, 3, 8), 8, 3)
    print "convert(convert(1120, 3, 9), 9, 3)\t-->\t", convert(convert(1120, 3, 9), 9, 3)
    print "convert(convert(1120, 3, 10), 10, 3)\t-->\t", convert(convert(1120, 3, 10), 10, 3)


def combi_plot_test():
    start = 10
    stop = 1000
    y_vals = [[math.log(i) for i in range(start, stop)],
              [i for i in range(start, stop)],
              [i**2 for i in range(start, stop)],
              [i**3 for i in range(start, stop)]]
    lbls = ['Logarithmic', 'Linear', 'Quadratic', 'Cubic']

    # Without x values defined
    combi_plot(y_vals, lbls)

    # With x values defined
    combi_plot(y_vals, lbls, [i*1000 for i in range(100, 100 + stop - start)])

    # Log-log plot
    combi_plot(y_vals, lbls, range(start, stop), True)

    # With everything defined
    combi_plot(y_vals, lbls, range(100, 100 + stop - start), True, 'Y-values', 'X-values', 'Combi Plot', ':')


def matrix_multi_test():
    a1 = [[1, 2, 3],
          [4, 5, 6]]

    b1 = [[7, 8],
          [9, 10],
          [11, 12]]

    a2 = [[3, 4, 2]]

    b2 = [[13, 9, 7, 15],
          [8, 7, 4, 6],
          [6, 4, 0, 3]]

    a3 = [[0, 2, 2],
          [0, 1, 3]]

    b3 = [[2, 1],
          [2, 0],
          [2, 0]]

    a4 = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

    m_print(matrix_multi(a1, b1))
    m_print(matrix_multi(a2, b2))

    m_print(matrix_multi(a3, b3))
    m_print(matrix_multi(b3, a3))

    m_print(matrix_multi(a4, a4))


    # Matrix multiplication can also be done with numpy's .dot:
    import numpy as np

    print np.dot(a3, b3)
    print np.dot(b3, a3)
    print

    # Note: Instead of lists, it is recommended to use numpy arrays:
    np_a3 = np.array(a3)
    np_b3 = np.array(b3)
    print np.dot(np_a3, np_b3)
    print np.dot(np_b3, np_a3)
    print


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


def time_func_test():
    # Run tests a couple of times for higher accuracy
    for i in range(3):
        print time_func(test1)("test1")
        print time_func(test2)("test", 2)
        print time_func(test3)("test", 1, 2)
        print
    del i

def test1(a_str):
    count = 0
    for i in range(1):
        count += 1
    print a_str

def test2(a_str, an_int):
    count = 0
    for i in range(10000):
        count += 1
    print a_str + str(an_int)

def test3(a_str, int1, int2):
    count = 0
    for i in range(100000):
        count += 1
    print a_str + str(int1+int2)


# =================================== Run tests ===================================

print "\n========== TEST: base_converter =========="
base_converter_test()

print "\n========== TEST: combi_plot =========="
combi_plot_test()

print "\n========== TEST: matrix_multi =========="
matrix_multi_test()

print "\n========== TEST: time_func =========="
time_func_test()

print "\n========== TEST: what_you_give =========="
print what_you_get(10)