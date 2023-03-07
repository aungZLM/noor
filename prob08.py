i = eval(input("Enter initial investment: "))
pp = eval(input("Enter purchase price: "))
sp = eval(input("Enter sell price: "))
p = sp - pp - i
if (p > 0):  print("Profit of", p)
elif (p == 0):  print("No profit or loss.")
else:  print("Loss of", p)