'''
What you give is what you get. Illustration of recursive functions.

Copyright (C) 2015-17 Niels Wadsholt
'''

def what_you_get(what_you_give):
    '''
    What you give is what you get.
    '''
    
    if what_you_give is 0:
        return 0
    
    return what_you_get(what_you_give - 1) + 1

