# Python Program Code to Calculate Grade of Student
score = input("Enter Score: ")
scoure = float(score) # convert
if scoure > 0.0 and  scoure < 1.0 :
    if scoure >= 0.9 :
        print("A")
    elif scoure >= 0.8 :
        print("B") 
    elif scoure >= 0.7 :
        print("C")
    elif scoure >= 0.6 :
            print("D") 
    else:
        print("F")
else :
    print("Error number is out of range")
        
