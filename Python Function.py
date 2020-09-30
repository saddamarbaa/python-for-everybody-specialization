# Python Functions
# A function is a block of code which only runs when it is called.
# simple function to say Hello
def function1():
    print("Hello from a function")
    print("so nice to meet You")
print("we are outside the function")
# call function
function1()

# Arguments
# simple mapping function
def map(x):
    return x*x
# call function
num = map(5)
print(num) # output will be 25
print(map(10)) # output will be 100

# function with multiy argument
def sum(x, y) :
    return x + y
# call function
num = sum(5, 10)
print(num) # output will be 15
print(sum(10, 10)) # output will be 20

# function with no return value
def no_Return(givenValue):
    print("in the function")
    print(givenValue)
    print("still in the function ")
# call function
no_Return("HI")

# simple function to convert kile matters to miles
def convert(miles):
    return 1.6 * miles
# call fuction
miles = 12
km = convert(miles)
print(miles, "is ",km)

# function with 2 arguments no return value
def my_function(name, email):
    print(name, email)
# function call
my_function("Jhon", "www.jhon.gmail.com")
my_function("ALi", "www.ali.gmail.com") 
my_function("sadam", "www.jhon.yahoo.com") 
# Default Parameter Value
def my_Name(name = "Saddam"):
  print("Hi nice meet you my name is " + name)
# function call
my_Name("ALI")
my_Name() # for this one output will be the Default Parameter Value 
my_Name('JHON')
my_Name("Mannura")
my_Name() # for this one output will be the Default Parameter Value

# Recursive function
def recursion_Function(n):
    if n > 0: # base cases
        print(n)
        recursion_Function(n - 1) # recursive cases
# function call
recursion_Function(10)
    
    
  
