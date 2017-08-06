'''
Base converter

Copyright (C) 2015-17 Niels Wadsholt
'''

def convert(num, old_base, new_base):
    '''
    Converts an integer from one base to another.
    
    Numbers are represented as actual base-10 integers (not strings). Works for
    base 2 through 10.
    '''
    
    assert 1 < old_base < 11 > new_base > 1, "The base must be between 2 and 10."
    
    if num == 0: # base case
        return 0
    elif num < 0: # handle negative numbers
        return -convert(-num, old_base, new_base)
    elif old_base != 10 and new_base != 10: # direct conversion only works to/from base 10        
        num = convert(num, old_base, 10)
        old_base = 10
    
    temp = num
    power = 0
    
    while temp >= new_base:
        temp /= new_base
        power += 1
    
    return old_base**power + convert(num - new_base**power, old_base, new_base)


def dec_to_bin(num):
    '''
    Converts a base-10 integer to its binary representation.
    '''
    
    return convert(num, 10, 2)


def bin_to_dec(num):
    '''
    Converts a binary integer to its base-10 representation.
    '''
    
    return convert(num, 2, 10)


# =================================== Test ===================================

# print dec_to_bin(42)
# print convert(42, 10, 2)
# print convert(101010, 2, 3)
# print convert(1120, 3, 2)
# print convert(convert(1120, 3, 4), 4, 3)
# print convert(0, 9, 3)
# print dec_to_bin(-42)
