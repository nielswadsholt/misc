'''
Test module for the misc library

Copyright (C) 2017 Niels Wadsholt
'''

import time
import numpy as np
from base_converter import *
from combi_plot import *
from matrix_multi import *
from time_func import *
from what_you_give import *


def base_converter_test():
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

    print "convert(52, 8, 2)\t-->\t", convert(52, 8, 2)
    print "convert(52, 8, 5)\t-->\t", convert(52, 8, 5)
    print "convert(52, 8, 7)\t-->\t", convert(52, 8, 7)
    print

    print "convert(-52, 8, 2)\t-->\t", convert(-52, 8, 2)
    print "convert(-52, 8, 5)\t-->\t", convert(-52, 8, 5)
    print "convert(-52, 8, 7)\t-->\t", convert(-52, 8, 7)
    print

    print "convert(convert(1120, 3, 2), 2, 3)\t-->\t", convert(convert(1120, 3, 2), 2, 3)
    print "convert(convert(15206, 7, 3), 3, 7)\t-->\t", convert(convert(15206, 7, 3), 3, 7)
    print

    print "dec_to_bin(42)\t-->\t", dec_to_bin(42)
    print "bin_to_dec(101010)\t-->\t", bin_to_dec(101010)
    print

    print "bin_to_dec(dec_to_bin(7))\t-->\t", bin_to_dec(dec_to_bin(7))
    print "dec_to_bin(bin_to_dec(111))\t-->\t", dec_to_bin(bin_to_dec(111))


def combi_plot_test():
    start = 10
    stop = 1000
    y_vals = [[math.log(i) for i in range(start, stop)],
              [i for i in range(start, stop)],
              [i**2 for i in range(start, stop)],
              [i**3 for i in range(start, stop)]]
    lbls = ['Logarithmic', 'Linear', 'Quadratic', 'Cubic']

    print "With only y values and labels defined ..."
    combi_plot(y_vals, lbls)

    print "Log-log plot ..."
    combi_plot(y_vals, lbls, range(start, stop), True)

    print "With everything defined ..."
    combi_plot(y_vals, lbls, range(100, 100 + stop - start),
               True, 'Y-values', 'X-values', 'Combi Plot (log-log)', [':', '-.', '--', '-'])


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
    
    print "Matrix multiplication can also be done with numpy's .dot:"
    print np.dot(a3, b3)
    print
    print np.dot(b3, a3)
    print
    print np.dot(a4, a4)
    print
    
    print "Note: Instead of lists, it is recommended to use numpy arrays:"
    np_a3 = np.array(a3)
    np_b3 = np.array(b3)
    np_a4 = np.array(a4)
    print np.dot(np_a3, np_b3)
    print
    print np.dot(np_b3, np_a3)
    print
    print np.dot(np_a4, np_a4)
    print
    
    print "Multiplying adjacency matrices:"
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
    print time_func(test1)("Test 1")
    print time_func(test2)("\nTest ", 2)
    print time_func(test3)("\nTest ", 1, 2)
    print "\nTest 4:\nPlotting running times ..."
    
    start = 10
    stop = 60
    
    log_array = np.zeros(stop - start, dtype=float)
    lin_array = np.zeros(stop - start, dtype=float)
    sqr_array = np.zeros(stop - start, dtype=float)
    cub_array = np.zeros(stop - start, dtype=float)
    
    for i in range(start, stop):
        log_array[i - start] = time_func(test4)(int(math.log(i)))
        lin_array[i - start] = time_func(test4)(i)
        sqr_array[i - start] = time_func(test4)(i**2)
        cub_array[i - start] = time_func(test4)(i**3)
    
    y_vals = [log_array, lin_array, sqr_array, cub_array]
    lbls = ['Logarithmic', 'Linear', 'Quadratic', 'Cubic']

    combi_plot(y_vals, lbls, range(start, stop), False, 'Time (ms)', 'n', 'Testing time_func()')
    
    print "\nTest 5:\nFibonacci numbers - regular recursive vs. dynamic programming"
    n = 25
    print "n = ", n
    print "Function:\tResult:\tTime:"
    print "fib()\t\t", fib(n), "\t", time_func(fib)(n)
    print "fib_dp()\t", fib_dp(n), "\t", time_func(fib_dp)(n)
    
    print "\nTest 6:\nPlotting Fibonacci running times ..."
    fib_array = np.zeros(n, dtype=float)
    fib_dp_array = np.zeros(n, dtype=float)
    
    for i in range(n):
        fib_array[i] = time_func(fib)(i + 1)
        fib_dp_array[i] = time_func(fib_dp)(i + 1)
    
    y_vals = [fib_array, fib_dp_array]
    lbls = ['Regular recursion', 'Dynamic programming']

    combi_plot(y_vals, lbls, range(n), False, 'Time (ms)', 'n', 'Computing the nth Fibonacci number', ['--', '-.'])

def test1(a_str):
    print a_str + ":"

def test2(a_str, an_int):
    count = 0
    for i in range(10000):
        count += 1
    print a_str + str(an_int) + ":"

def test3(a_str, int1, int2):
    count = 0
    for i in range(100000):
        count += 1
    print a_str + str(int1+int2) + ":"

def test4(n):
    for i in range(n):
        time.sleep(0.000000001 * i)

def fib(n):
    '''
    Returns the nth Fibonacci number.
    '''
    if n <= 2:
        return n > 0
    else:
        return fib(n - 1) + fib(n - 2)

def fib_dp(n, memo = {}):
    '''
    Returns the nth Fibonacci number. Dynamic programming version using memoization.
    '''
    if n in memo:
        return memo[n]
    elif n <= 2:
        return n > 0
    else:
        memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
        return memo[n]


# =================================== Run tests ===================================

print "\n\n==================== TEST: base_converter ====================\n"
base_converter_test()

print "\n\n==================== TEST: combi_plot ====================\n"
combi_plot_test()

print "\n\n==================== TEST: matrix_multi ====================\n"
matrix_multi_test()

print "\n\n==================== TEST: time_func ====================\n"
time_func_test()

print "\n\n==================== TEST: what_you_give ====================\n"
print "what_you_get(10) --> ", what_you_get(10)