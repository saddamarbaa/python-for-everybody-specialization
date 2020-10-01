""" Assignment 10.2
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

name = input("Enter file:") # user input
# Error handling use default file name 
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name) # open file
counts = dict()   # create Empty Dictionary

for word in handle :      # iterate over the file read line by line
  word = word.rstrip()    # remove spaes
  if not word.startswith('From ') : continue
  message = word.split() # splie  the  word(message)
  Time  = message[5]   # get the time
  hour = Time[: 2]    # get the hour
  #print(hour)  # only for testing
  # count the words and add to dictionary
  counts[hour] = counts.get(hour, 0) + 1

#print(counts) # only for testing
# create Empty List (list of Tuple)
tuple_List = list()

# Iterate over the counts list and build tuple in  Key value order
for key, value in counts.items() :
  newtupe =(key, value)  # get the key value 
  tuple_List.append(newtupe) # append the key, value in tuple list

# Now let sort the tuple list for that let call sorted function
# (reverse = false) mean sort the list from smallest to biggest value 
tuple_List = sorted(tuple_List, reverse = False)

# print the sorted tuple
#print()
#print(tuple_List) # only for testing

# iterate over the sorted tuple and print it
for key, value in tuple_List :
  print(key, value) # now print the value key order
