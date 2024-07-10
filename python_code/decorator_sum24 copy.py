#Functions are first-class objects.

# Add functionality to an existing function with decorators. 
# This is called metaprogramming.

# A function can take a function as argument (the function to be decorated) and #return the same function with or without extension.
# Extending functionality is very useful at times, we’ll show real world examples # 3 # later in this file.

# Python decorators are functions that takes in a function and returns it by adding some functionality

#--------------------------------------------------------
# Example of function as 1st-class object
def func1():
    print("This is a function")

# I can assign a function to a variable, because in Python functions
# are 1st class objects 
another_func = func1
another_func()


print()
#--------------------------------------------------------
# Example of nested functions
# Passing exponents to a number
def outer1(exp):
    def inner(num):
        return num ** exp
    return inner

add_exps = outer1(5)

# the above equals this
# def outer1(5):
#     def inner(num):
#         return num ** 5
#     return inner

result = add_exps(6)
print(result)


print()
#--------------------------------------------------------
# Basic functionality of a decorator
def authenticator(func):
    print("The decorator function has been called")
    def wrapper():
        print("Beginning of the wrapper function")
        func()
        print("End of the wrapper function")
    return wrapper

def some_view():
    print("I'm a django view")

# Decorating the function by passing the some_view function to the authenticator
# The authenticator returns the wrapper function and assigns it to a variable
result = authenticator(some_view)

# Calling the wrapper function
result()

#-----------------------OR---------------------------------
print()

# Line 34 is from line 12 above
@authenticator
def some_view():
    print("I'm a plain ol' django view")

some_view()