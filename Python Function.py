"""
Python Functions
for Reference 
Lec 4 | MIT 6.00 Introduction to Computer Science and Programming, Fall 2008
link:
https://youtu.be/SXR9CDof7qw
A function is a block of code which only runs when it is called.
"""

def sqrt(x):    
    """
    (Lec 3 | MIT Fall 2008)
    Return the square root of x if x is perfect square
    print an Error Message and  Return None otherwise
    """
    answer = 0 # counter
    if x >= 0:
        while answer * answer < x:
            answer += 1 # increment counter by one
            #print(f"answer : {answer}")
            if answer * answer != x:
                print(f"{answer} is not a perfect square root") 
                #return None
            else:
                print(f"{answer} is a perfect square root")
                return answer
    else:
        print(f"Error {n} is a negative number")
        return None

# function call
print(sqrt(16)) # will return 4
#print(sqrt(15)) # will return None

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
def recursion_function(n):
    if n > 0: # base cases
        print(n)
        recursion_function(n - 1) # recursive cases
# function call
recursion_function(10)


def fib(x): 
    """
    Recursive function Return finbonacci Sequence of x where x is a none
    negative int
    """
    #if x == 0 or x == 1 or x == 2: # base case
    if x <= 2: # base case
        return 1
    else : # Recursive case
        return fib(x - 1) + fib(x - 2)
    
# function call
# testing
print(fib(2)) # output 1
print(fib(3)) # output 2
print(fib(4)) # output 3
print(fib(8)) # output 21
print(fib(9)) # output 34
print(fib(15)) # output 610


def fib_memorization(x, memo): 
    """
    Dynamic Programming Fibonacci Sequence(Recursion with memorization)
    Recursive function to calculate and return Fibonacci Sequence of x
    assuming that x is positive integer 
    """
    if x == 1 or x == 2: # one of base cases
        return 1
    
    # if fib(x) is in the memory return fib(n)
    if memo[x] is not None:
        return memo[x] # second base cases
    # in else case calculate fib(x) save in memory first then returned
    else:
        result = fib_memorization(x - 1, memo) + \
            fib_memorization(x - 2, memo)
    return result

# function call
# testing
# create memorization list store all None and call function
x = 3
memo = [None] * (x + 1)
Rseult = fib_memorization(x, memo)
print(Rseult)
"""
# for testing
x = 5
memo = [None] * (x + 1)
Rseult = fib_memorization(x, memo)
print(Rseult)
"""
"""
# for testing
x = 9
memo = [None] * (x + 1)
Rseult = fib_memorization(x, memo)
print(Rseult)
"""

def fib_bottom_up(x): 
    """
    Dynamic Programming Fibonacci Sequence(bottom up approach)
    function to calculate and return Fibonacci Sequence of x
    assuming that x is positive integer
    """
    if x == 1 or x == 2: # one of base cases
        return 1
    
    # create bottom up list 
    bottom_up = [None] * (x + 1)
    # Fibonacci Sequence  of 1 and 2 is one
    bottom_up[1] = 1
    bottom_up[2] = 1
    # Iterate over the list in range 3 to x+1 
    # and calculate the Fibonacci Sequence    
    for i in range(3, x+1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2] 
    # now return the Fibonacci Sequence given number x
    return bottom_up[x]
        

# function call
# testing
#print(fib_bottom_up(2))
#print(fib_bottom_up(7))
#print(fib_bottom_up(4))
#print(fib_bottom_up(35))
#print(fib_bottom_up(100))
#print(fib_bottom_up(1000))
print(fib_bottom_up(10000))

