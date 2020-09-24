# small program to calculate hourly Pay 
# user input
hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
# Exceptions Handling
try: 
   hrs = float(hrs)
   rate = float(rate)
except:
   print("Eror please Enter Numeric Number:")
   quit() # is done
# calculate result
if hrs > 40:
    reg = hrs* rate
    outp = (hrs - 40.0) * (rate * 0.5)
    exp = reg  + outp
    print(exp)
else:
   exp = hrs* rate
   print(exp)
   
  
