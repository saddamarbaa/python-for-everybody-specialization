""" Assignment 9.4
 Write a program to read through the mbox-short.txt and figure 
 out who has sent the greatest number of mail messages. 
 The program looks for 'From ' lines and takes the second word of those 
 lines as the person who sent the mail. The program creates a Python dictionary 
 that maps the sender's mail address to a count of the number of times they appear 
 in the file. After the dictionary is produced, 
 the program reads through the dictionary using a maximum loop to find the most prolific committer."""

name = input("Enter file:") # user input
# Error handling use default file name 
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name) # open file

counts = dict()   # create Empty Dictionary

for line in handle :      # iterate over the file read line by line
  line = line.rstrip()    # remove spaes
  if not line.startswith('From '): continue
  words = line.split() # splie line into words
  word = words[1]
  #print(word)  # only for testing

  # count the words and add to dictionary
  counts[word] = counts.get(word, 0) + 1
#print(counts) # only for testing
  
"""counter variables to uses in for loop wile searching for
person with greatest number of mail messages """
largest = -1
person = None
# iterate over the dictionary
for key, value in counts.items() :
  # if you found new largest word then update largest and  person
  if value > largest :
    largest = value   # the largest so far
    person = key      # in key value

# Finally print the largest found
print(person, largest)

