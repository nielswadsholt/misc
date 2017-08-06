"""
Timer for meassuring running time of functions with varying numbers of parameters.

By Niels Wadsholt, January 2016
"""


def time_func(func):
    """
    Returns a function timer with the number of parameters defined by
    the timed function. The timer returns elapsed time in milliseconds.
    """
    
    def timer(*args):
        """
        Function timer with the number of parameters defined by
        the timed function. Returns elapsed time in milliseconds.
        """
        
        import time
        
        time1 = time.clock()
        func(*args)
        time2 = time.clock()
        
        return (time2 - time1) * 1000
    
    return timer


# ========== TESTING ==========

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

def time_func_test():
    # Run tests a couple of times for higher accuracy
    for i in range(3):
        print time_func(test1)("test1")
        print time_func(test2)("test", 2)
        print time_func(test3)("test", 1, 2)
        print
    del i

# test()

