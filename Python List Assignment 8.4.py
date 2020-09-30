""" Assignment 8.4
 8.4 Open the file romeo.txt and read it line by line. For each line, 
 split the line into a list of words using the split() method. 
 The program should build a list of words. 
 For each word on each line check to see if the word is already 
 in the list and if not append it to the list.
 When the program completes, sort and print the resulting words in alphabetical order.

You can download the sample data at http://www.py4e.com/code3/romeo.txt   """

givenFile = input("Enter file name: ") # user input
givenFile = open(givenFile)  # open file
lst = list()                # create Empty List
for line in givenFile :    # iterate over the file
  line = line.rstrip()    # remove spaes
  words = line.split()  # split line to small word
  #print(words)
  for line in words :   # iterate over the word
    if line not in lst :
      lst.append(line)  # if the word is not on list add to list
lst.sort()      # sort the list
print(lst)     # print the list
