# python function to computes the gross salary.
# user input
# define function
def computepay(hrs, rate):
    # calculate result
    if hrs > 40 :
        reg = hrs * rate
        outp = (hrs - 40.0) * (rate * 0.5)
        finalResult = reg  + outp
        
    else :
        finalResult = hrs * rate
    return finalResult # return the result
# user input
hrs = float(input("Enter Hours:"))
rate = float (input("Enter rate:"))
# function call
p = computepay(hrs,rate)
print("Pay",p)
