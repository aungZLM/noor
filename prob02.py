classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
percentage = (classes_attended / classes_held) * 100
print("Percentage of class attended:", percentage)
if (percentage < 75):  
    print("Student is not allowed to sit in exam.")
else:  
    print("Student is allowed to sit in exam.")