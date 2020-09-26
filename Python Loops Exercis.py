# Programming for Everybody (Getting Started with Python)
# Exercise: 5.1(Chapter five)
# Write a program that repeatedly prompts a user for integer numbers until 
# the user enters 'done'. Once 'done' is entered, print out the largest and 
# smallest of the numbers. If the user enters anything other than a valid 
# number catch it with a try/except and put out an appropriate message and
# ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True :
   value = input("Enter a number: ")
   if value  == "done" : # if user enter done break the loop
       break
   try :  # exception hundlling
       value = int(value)
   except :
       print("Invalid input")
       continue # go back and continue
   if largest == None :
        largest = value 
   if smallest  == None :
       smallest  = value
   elif value < smallest :
       smallest  = value # Minimum so far
   elif value > largest :
       largest = value  # Maximum so far 
       
# print the result
print("Maximum is", largest)
print("Minimum is", smallest)
