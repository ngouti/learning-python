#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")
    # python uses scope definer (colon) & indentation

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for z in args:
        result = result + z
    return result


func1() 
# function being called directly
print (func1())
# function being called in print function, then outer print fX executes
# our function doesnt return value so Python evalutes return value to be None 
# I am a function
# None
print (func1)
# were just print the function value which is an object
# <function func1 at 0x0477B390>

func2(10,20)
print (func2(10,20))
print (cube(3))
print (power(2))