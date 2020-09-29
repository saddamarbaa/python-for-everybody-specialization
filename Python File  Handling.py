# File Handling in Python

try:
  # Open file in current directory
  fName = open("words.txt", mode ='r')
  # Open a file on a different location
  fhand = open("E:\\files\python.txt", mode='r') 
  
  # This will print every line one by one in the file 
  for line in fName :
    line = line.rstrip()  # remove new
    print(line) 

  # Read from file
  fhand .read()     # read all the file
  fName.read(2)    # read the first 2 data
  fName.read(3)    # read the next 4

  # Read Lines from file   
  print(fName.readline())
  print(fName.readline())

  # Create file in write() mode
  newfile = open("texz.txt", mode ='r')
  newfile .write("let write to file") 
  newfile .write("let wirte more and more")

  # Write to an Existing File
  file = open("E:\\files\python.txt", mode ='a') 
  file.write("add new word ")

except:
  print("file cant open")
  quit()
  
# Closing File 
fhand.close()
fName.close()
file.close()
