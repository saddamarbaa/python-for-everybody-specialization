# Python Dictionaries
# {key , value}

dictionary = {} # Create empty dictionary

# create phone Book dictionary 
phoneBook = {"Bob" : "12-237373", 
            "Ali"  : "2137373",
            "Joli" : "32736462",
            "Mnaue": "21732_8383"}

# create dictionary with mixed keys
dict1 = {'name': 'Sadam', 1: [1, 2, 3]}

print(phoneBook) # print Dictionary
phoneBook["Adam"] = "123455" # add to Dictionary
print(phoneBook) # print Dictionary
print(phoneBook['Ali'])
print(dict1) # print Dictionary

# Accessing Elements from Dictionary
print(phoneBook.get('Adam')) # Output: Adam
print(dict1.get('name'))     # output  name

# Changing and adding Dictionary Elements
phoneBook = {"Bob" : "54239493", "Joli" : "32736462", "Soli" : "32736462" }

# update value
phoneBook['Ali'] = "63626_82837"

# add new  item
phoneBook['Sali'] = '663621_12'

# now print Dictionary
print(phoneBook)

# Loop Through a Dictionary
for name in phoneBook :
  print(name)
print() # new line
for name in dictionary :
  print(name)

# Check if Key Exists in phoneBook
if "Ali" in phoneBook :
  print("Yes, 'Ali Exists") 
else :
  print("Not, 'Ali not Exists")

# Removing elements from a dictionary
print(phoneBook.pop("Ali")) # remove Ali
print(phoneBook)
print(phoneBook.pop("Sali")) # remove Sali
print() # new line 
print(phoneBook)

# delete elements from a dictionary using del keyword
del phoneBook["Soli"] # delete Soli
print()
print(phoneBook)

# Copy a Dictionary
copyphoneBook = {} # create Empy dictionary
# now copy phoneBook to copyphoneBook
copyphoneBook = phoneBook.copy
print(copyphoneBook) # print copyphoneBook

# Dictionary Length
print(len(phoneBook))
print(len(dict1))
print(len(dictionary))

# clear Dictionary
phoneBook.clear()
dictionary.clear()
