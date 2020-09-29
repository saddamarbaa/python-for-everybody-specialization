
# Assignment 7.2 in week 3
""" 
Count these lines and extract the floating point values from each of the lines and compute
the average of those values and produce an output . Do not use the sum() function or a variable
named sum in your solution. 
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name. """

# user input 
fname = input("Enter file name: ")
fhand = open(fname) # Opening Files
count = 0 # counter
total = 0 # for total
for line in fhand : # loop and Read from file
    if line.startswith("X-DSPAM-Confidence:") :
        count += 1  # increment count
        # extract the floating point values from each of the lines
        floatValue = float(line[20:]) 
        total += floatValue # compute the total sum 
result = total / count # compute the average 
print("Average spam confidence:", result)
