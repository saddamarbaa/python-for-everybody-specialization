# Python Strings
# Strings declarations
name = "saddam arbaa"
job = "Web Programmer"
# Multiline Strings
message = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print
print("Name:", name)
print("Job:", job)
print("message:", message)
# String Concatenation
firstName = input("Enter Your first name: ")
lastName = input("Enter Your last name: ")
# Concatenation
fullName = firstName + " " + lastName
print("Yor Full Name is ",fullName)

# for test only
test = 'Concatenation'
# output "Concat"
print(test[0] + test[1] + test[2] + test[3] + test[4] + test[5])
# output "ion" Backward Indexing
print(test[-3] + test[-2] + test[-1])
# print characters from position 3 to position 6
print(test[3 : 6])
# print characters from position 6 to position 3 (Negative Indexing)
print(test[-6 : -3])
# String Length
print(len(test))
# lower()
print(test.lower())
# upper()
print(test.upper())
# replace() method replaces a string with another string :
print(test.replace("a", "?"))
# print from index 3 to last index
print(test[3:])
# Check String
print("ion" in test)
# String Format
name = "saddam arbaa {} {}"
age = 30
id = 212
print(name.format(age, id))
