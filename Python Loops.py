"""
Python Loops
for Reference 
Lec 3 | MIT 6.00 Introduction to Computer Science and Programming, Fall 2008
link:
https://youtu.be/X6ilT3uUOBo 
"""
# Python While Loop
# Print i as long as i is less than 10  
i = 1
while i < 10:
    print(i)
    i = i + 1 # increment i by one
print("this is after while loop")

# Calculate sum of posstive number in this sorted list
list = [5, 4, 3, 1, -3, -6]
sum = 0
i = 0
while list[i] > 0 :
    sum += list[i]
    i += 1
print("sum is  = ", sum)

# find the square Root of a perfect square(Lec 3 | MIT Fall 2008)
n = 16  
answer = 0 # counter
if n >= 0:
    while answer * answer < n:
        answer += 1 # increment counter by one
        print(f"answer : {answer}")
        if answer * answer != n:
            print(f"{answer} is not a perfect square root") 
        else:
            print(f"{answer} is a perfect square root") 
else:
    print(f"Error {n} is a negative number") 

# find find all the divisor of  N (Lec 3 | MIT Fall 2008)
n = 10 
i = 1 # counter
while i < n:
    if n % i == 0:
        print(f"{i} is divisor")
    i += 1 # increment counter by one
            
# The break Statement with while loop
i = 1
while i < 10:
    print(i)
    if i == 6:
        break
    i = i + 1 # increment i by one
print("this is after The break Statement")

# The break continue with while loop
i = 0
while i < 10:
    i += 1 # increment i by one
    if i == 6:
        continue
    print(i)    

print("this is after The continue Statement")

# The else Statement
i = 1
while i < 10:
    print(i)
    i = i + 1 # increment i by one
else:
    print("condition is false now")

# Python For Loops
student = ["Jhon", "Manar", "Ali", "Nincy"]
for i in student :
    print(i)

# The break Statement with for loop
for i in student :
    if i == "Manar":
        break
    print(i)
print("this is after The break Statement")

# The continue Statement with for loop
for i in student :
    if i == "Manar":
        continue
    print(i)
print("this is after The break Statement")

myName = ("Saddam Arbaa")
for x in myName :
    print(x)

# The range() Function
for i in range(10) :
    print(i)
# The range() Function
# print number from 2 to 7
for i in range(2, 7) :
    print(i)
    
# print number from 5 to 25 (25 not included)
# increment i by 5
for i in range(5, 25, 5):
    print(i)
    
# sum of list
list = [2,3,4,5]
total = 0
for i in list:
    total += i
print("total is ", total)
    
# Else in For Loop
# print number from 2 to 22 (22 not included)
# increment i by 2
for i in range(2, 22, 2):
    print(i)
else :
    print("i is 22 now we are done")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:  # outer loop
  for y in fruits: # Nested Loops
    print(x, y)

# find sum of all the digits in given number(Lec 3 | MIT Fall 2008)   
sumdigit = 0 # counter
# convert the number to string and iterate digit by digit
for i in str(1952):
    # for each digit convert back to int and add to sumdigit
    sumdigit += int(i)
print(sumdigit)
    
    
    
