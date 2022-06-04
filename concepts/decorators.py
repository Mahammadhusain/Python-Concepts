# ------------ Python Decorator (# Calling way-1) ------------
def mydecorator(fn):
    def inner_function():        
        fn()
        print('How are you?')
    return inner_function

def greet():
	print('Hello! ', end='')


a=mydecorator(greet) 
a()

# ------------ Python Decorator (# Calling way-2) ------------
def mydecorator(fn):
    def inner_function():        
        fn()
        print('How are you?')
    return inner_function

@mydecorator
def greet():
	print('Hello! ', end='')

greet()

# NOTES - In Python Decorator is function
      # - Also take function as an argument
      # - and it return also function
