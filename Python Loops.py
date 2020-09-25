# Python Loops
# Python While Loops
# Print i as long as i is less than 10:
i = 1
while i < 10:
    print(i)
    i = i + 1 # increment i by one
print("this is after while loop")

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
