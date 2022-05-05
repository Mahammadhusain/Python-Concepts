def square(x):
    assert x>=0, 'Only positive numbers are allowed'
    return x*x

n = square(2) # returns 4
print(n)
n = square(-2) # raise an AssertionError
print(n)