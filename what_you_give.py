# What you give is what you get
# Illustration of recursive functions
# Idea and implementation by Niels Wadsholt, 2015

def what_you_get(what_you_give):
    if what_you_give is 0:
        return 0
    what_you_give -= 1
    return what_you_get(what_you_give) + 1

