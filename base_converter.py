def dec_to_bin(num):
    '''
    Converts a decimal number to it's binary representation
    '''
    
    return convert(num, 10, 2)


def bin_to_dec(num):
    '''
    Converts a binary number to it's decimal representation
    '''
    
    return convert(num, 2, 10)


def convert(num, old_base, new_base):
    '''
    Converts a number from one base to another. Works for base 2 through 10.
    '''
    
    assert 1 < old_base < 11 > new_base > 1, "The base must be between 2 and 10."
    
    if num < 1: # base case
        return 0
    elif old_base != 10 and new_base != 10: # direct conversion only works to/from base 10        
        num = convert(num, old_base, 10)
        old_base = 10
    
    temp = num
    power = 0
    
    while temp >= new_base:
        temp /= new_base
        power += 1
    
    return old_base**power + convert(num - new_base**power, old_base, new_base)


# =================================== Test ===================================

def test():
    print dec_to_bin(42)
    print bin_to_dec(101010)
    print

    print bin_to_dec(dec_to_bin(7))
    print dec_to_bin(bin_to_dec(111))
    print

    print bin_to_dec(0)
    print bin_to_dec(1)
    print bin_to_dec(10)
    print bin_to_dec(11)
    print bin_to_dec(100)
    print bin_to_dec(101)
    print bin_to_dec(110)
    print bin_to_dec(111)
    print bin_to_dec(1000)
    print bin_to_dec(1001)
    print bin_to_dec(1010)
    print bin_to_dec(1011)
    print bin_to_dec(1100)
    print bin_to_dec(1101)
    print bin_to_dec(1110)
    print bin_to_dec(1111)
    print

    print dec_to_bin(0)
    print dec_to_bin(1)
    print dec_to_bin(2)
    print dec_to_bin(3)
    print dec_to_bin(4)
    print dec_to_bin(5)
    print dec_to_bin(6)
    print dec_to_bin(7)
    print dec_to_bin(8)
    print dec_to_bin(9)
    print dec_to_bin(10)
    print dec_to_bin(11)
    print dec_to_bin(12)
    print dec_to_bin(13)
    print dec_to_bin(14)
    print dec_to_bin(15)
    print

    print convert(42, 10, 2)
    print convert(42, 10, 3)
    print convert(42, 10, 4)
    print convert(42, 10, 5)
    print convert(42, 10, 6)
    print convert(42, 10, 7)
    print convert(42, 10, 8)
    print convert(42, 10, 9)
    print convert(42, 10, 10)
    print

    print convert(101010, 2, 10)
    print convert(1120, 3, 10)
    print convert(222, 4, 10)
    print convert(132, 5, 10)
    print convert(110, 6, 10)
    print convert(60, 7, 10)
    print convert(52, 8, 10)
    print convert(46, 9, 10)
    print convert(42, 10, 10)
    print

    print convert(101010, 2, 2)
    print convert(101010, 2, 3)
    print convert(101010, 2, 4)
    print convert(101010, 2, 5)
    print convert(101010, 2, 6)
    print convert(101010, 2, 7)
    print convert(101010, 2, 8)
    print convert(101010, 2, 9)
    print convert(101010, 2, 10)
    print

    print convert(52, 8, 2)
    print convert(52, 8, 3)
    print convert(52, 8, 4)
    print convert(52, 8, 5)
    print convert(52, 8, 6)
    print convert(52, 8, 7)
    print convert(52, 8, 8)
    print convert(52, 8, 9)
    print convert(52, 8, 10)

# test()