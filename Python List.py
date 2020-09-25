# Python Lists
thislist =[1, 2, 3, 4, -1]
print(thislist)
# Add Items to list
thislist.append(12)
print(thislist)
thislist.append("hello")
print(thislist)
# add list to lsit
thislist.append([12,3])
print(thislist)

# delete last Items from list
# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)
thislist.pop()
print(thislist)
print(thislist[0])
print(thislist[3])

# Remove Items from list
thislist.remove(2)
print(thislist)

# change thislist[3] to 100
thislist[3] = 100
print(thislist)
furit = ["apple", "banana", "cherry", "orange", "melon", "mango"]
print(furit[1])
print(furit)
# swap furit[0] and furit[2]
furit[0], furit[2] = furit[2], furit[0] 
print(furit)
print(furit[-1]) # print the last one index value
print(furit[2 : 5]) # print from 2 to 5
print(furit[: 3]) # print from 0 to 3
print(furit[3 :]) # print from 3 to last
# This example returns the items from index -4 (included) to index -1 (excluded)
print(furit[-4 : -1])

# Loop Through a List
for i in furit:
  print(i)
  
# Check if Item Exists
# Loop Through a List
for i in furit:
  if "banana" in furit:
       print("banana in the list") 
       break

#List Length
print(len(furit))
print(len(thislist))
 
# Remove Items from list
furit.remove("banana")
print(furit)

# Copy a List
newlist = furit.copy()
print(newlist)

# Join Two Lists
firstList = [1,2,3,4]
secondList =[5,6,7,8,9]
joinedList = firstList + secondList
print(joinedList)
# loop over second list and append in firstList 
for i in secondList:
    firstList.append(i)
print(firstList)

# clear the list
# The clear() method empties the list:
furit.clear()
print(furit) # furit list is empty now
thislist.clear()
print(thislist) # thislist is empty now
