id = int(input("Enter customer ID: "))
name = input("Enter Customer Name: "))
units_consumed = int(input("Enter units consumed: "))
# calculate bill
amount_due = 0
if (units_consumed <= 199):  amount_due = units_consumed * 1.20
elif (units_consumed <= 399):  amount_due = (199*1.20) + ((units_consumed - 199)*1.50)
elif (units_consumed <= 599):  amount_due = (199*1.20) + (200*1.50) + ((units_consumed-399)*1.80)
else:  amount_due = (199*1.20) + (200*1.50) + (200*1.80) + ((units_consumed-599)*2.00)
# apply surcharge
if (amount_due > 400):  amount_due = amount_due + (amount_due * 0.15)
# check for minimum bill
if (amount_due < 100):  amount_due = 100
print("Customer Name:", name)
print("Units Consumed:", units_consumed)
print("Amount Due: BDT.", format(amount_due,',.2f'))