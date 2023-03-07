side1 = eval(input("Enter side 1: "))
side2 = eval(input("Enter side 2: "))
side3 = eval(input("Enter side 3: "))
if (side1 == side2 == side3):  
    print("The triangle is Equilateral.")
elif (side1 == side2 or side2 == side3 or side1 == side3):  
    print("The triangle is Isosceles.")
else:  print("The triangle is Scalene.")
