
# Programming for Everybody (Getting Started with Python)
# Exercise: 5.1(Chapter five)
num = 0
total = 0.0
while True :
   value = input("Enter Number: ")
   if value  == "done" : # if user enter done break the loop
       break
   try :  # exception hundlling
       value = float(value)
   except :
       print("Invalid  input!")
       continue # go back and continue
   num += 1  # count
   total += value # sum of all number
# print the result
print(total, num, total / num)
