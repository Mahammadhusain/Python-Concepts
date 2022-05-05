# ------------------------------------------------------------------------------------------------
#                                generator
# ------------------------------------------------------------------------------------------------


"""
Python provides a generator to create your own iterator function. 
A generator is a special type of function which does not return a single value, 
instead, it returns an iterator object with a sequence of values. In a generator function, 
a yield statement is used rather than a return statement. The following is a simple generator function.

"""

# Create Simple generator 
def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

# gen = mygenerator() 
# next(gen) # get First item
# next(gen) # get First item
# next(gen) # get First item
# next(gen) # throw error StopIteration

# stop generator using return
def mygenerator():
    print('First item')
    yield 10

    return

    print('Second item')
    yield 20

    print('Last item')
    yield 30 

# generator with for loop
def get_sequence_upto(x):
    for i in range(x):
        yield i

seq = get_sequence_upto(3)
print(next(seq)) # get First item 
print(next(seq)) # get First item
print(next(seq)) # get First item
print(next(seq)) # throw error StopIteration 