# Python Tuples
# A tuple is a collection which is ordered and unchangeable(Immutable)

# Different types of tuples
empyT = ()        # Empty tuple
print(empyT)

test_tuple = (1,) # Tuple With One Item
print(test_tuple)

numbers = (10, 20, 30, 40, 50 , 123)  # Tuple having integers only 
print(numbers) 

# tuple with mixed datatypes
mix_tuple = (1, "Hello", 3.4, '12', 'see you there') 
print(mix_tuple)

# nested tuple
nested_tuple = ("one", [8, 4, 6], (1, 2, 3) , "Two")
print(nested_tuple)

# Access Tuple Items
test_tuple = (1, 3 , 2, 'a')
print(test_tuple[1]) # Output: '3'
print(test_tuple[0]) # Output: '1'

# Negative Indexing
print(test_tuple[-1]) # Output: 'a'
print(test_tuple[-2]) # Output: '2'

# Slicing
test_tuple = (1, 3 , 2, 'a', 4, 56, 76, 23, 89, 12)

# print elements from 3nd to 6th
# Output: ('a', 4, 56)
print(test_tuple[3 : 6])

# print elements from beginning to 4nd
# Output: (1, 3 , 2, 'a')
print(test_tuple[ : 4])

# print elements from 4th to end
# Output: (4, 56, 76, 23, 89, 12)
print(test_tuple[4 :])

# print elements from beginning to end
# Output: (1, 3 , 2, 'a',4, 56, 76, 23, 89, 12)
print(test_tuple[ : ])

# Range of Negative Indexes
# Output: (56, 76, 23, 89, 12)
print(test_tuple[ -5 :  -1])

#  Iterating Through a Tuple
test_tuple = (1, 3 , 2, 'a',4, 56, 76, 23, 89, 12)
for item in test_tuple :
  print(item) 

# Tuple Length
print(len(test_tuple))

# Tuples and Assignment
(x, y) = (12, "Adam")
print(x, y)  # Output: (12, Adam)
print(y)  # Output: (Adam)
print(x)  # Output: (12)

# Tuples and Dictionaryies

d = dict() # create dictionary
d['casv'] = 2
d['cwen'] = 12
for (k, v) in d.items():
  print(k, v)

tups = d.items() #  d.items() give us tuple
# dict_items([('casv', 2), ('cwen', 12)])
print(tups)

# Sorting List of Tuples
# dictionary
d = {'M' : 10, 'B' : 1, 'C' : 22, 'W' : 2, 'A' : 21}
 
d.items() # make typles(convert Dictionary to Tuple)
# dict_items([('M', 10), ('B', 1), ('C', 22), ('W', 2)])
print(d.items())

# call sorted function
# [('A', 21), ('B', 1), ('C', 22), ('M', 10), ('W', 2)]
print(sorted(d.items())) # but this print sorted tuples in key order

# Sort tuple by values instead of KeyboardInterrupt
# dictionary
d = {'M' : 10, 'B' : 1, 'C' : 22, 'W' : 2, 'A' : 21}
# make temp tuple (lsit of tuple)
temp = list()
for key, value, in d.items() :
  temp.append((value, key)) # full the temp list
  
# [(10, 'M'), (1, 'B'), (22, 'C'), (2, 'W'), (21, 'A')]
print(temp)

# Now sort the temp tuples
# reverse = True mean sort from bigges value to smallest value
temp = sorted(temp, reverse = True) 

# print temp after been sorted by value
# [(22, 'C'), (21, 'A'), (10, 'M'), (2, 'W'), (1, 'B')]
print(temp)

 
