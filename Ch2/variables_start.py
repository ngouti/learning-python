# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0 
print(f)

# # re-declaring the variable works
f = "abc"
print (f)


# # ERROR: variables of different types cannot be combined
print ("string type " + str(123))
    # str convert number to string

# Global vs. local variables in functions
def someFunction():
  #global f
    #tells the function that f is now global, outputs def, def twice   
  f = "def"
  print (f)

someFunction()
print (f) 

# del f 
#  del undefines a variable in real time
# print(f)