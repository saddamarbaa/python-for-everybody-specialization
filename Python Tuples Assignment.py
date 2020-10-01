#  print the 10 most commom words in Dictionary

name = input("Enter file:") # user input
# Error handling use default file name 
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name) # open file

counts = dict()   # create Empty Dictionary

for line in handle :      # iterate over the file read line by line
  line = line.rstrip()    # remove spaes
  words = line.split() # splie line into words
  for word in words :
    #print(word)  # only for testing
    # count the words and add to dictionary
    counts[word] = counts.get(word, 0) + 1

#print(counts) # only for testing
# create Empty List (list of Tuple)
tuple_List = list()

# Iterate over the counts list and build tuple in Reverse Key value
for key, value in counts.items() :
  newtupe =(value, key)  # get the key value in Reverse
  tuple_List.append(newtupe) # append the value key in tuple list
  
print(tuple_List) # only for testing

# Now let sort the tuple list for that let call sorted function
# (reverse = True) mean sort the list from biggest value to smallest
tuple_List = sorted(tuple_List, reverse = True)

# print the sorted tuple
print()
print(tuple_List) # only for testing

# iterate over the sorted typle and print the 10 most commom words
print("The Top Most Common Words Are : ")
for key, value in tuple_List[: 10] :
  print(value, key) # now print the value key order
