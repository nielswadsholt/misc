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


def dec_to_bin(num):
    '''
    Converts a decimal number to its binary representation
    '''
    
    return convert(num, 10, 2)


def bin_to_dec(num):
    '''
    Converts a binary number to its decimal representation
    '''
    
    return convert(num, 2, 10)

