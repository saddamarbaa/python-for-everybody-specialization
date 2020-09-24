# Python Conditional Statement

# IF statement
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
if num1 >  num2:
   print("num1 greater than  num2")
elif num2 >  num1:
    print("num2 greater than  num1")   
else :
     print("num1 and num2 are equal")
     
# Ternary Operators
num1 =23
if num2 > num2: print("num is greater than num")
# And
if num1 > num2 and num1 > num3 :
    print("num1 is greaterst one")
# or
if num1 > 0 or num1 > 0 or num3 > 0 :
    print("at least one number is postive")

# Nested If
if num3 >= 0:
   if num3 == 0: # Nested If
       print("num3 is Zero")
   else :
      print("num3 Positive number")
else :
   print("num3 is Negative number")
