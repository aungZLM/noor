num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):  
    largest = num1
elif (num2 >= num1) and (num2 >= num3):  
    largest = num2
else:  
    largest = num3  
print("The largest number is",largest)