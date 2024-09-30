units = int(input("please enter number of units you consumed : "))
if(units < 50):
    amount = units * 2.60
    surcharge = 25
elif(units < 100):
    amount = 130 +((units - 50) * 3.25)
    surcharge = 35
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 50) * 5.62)
    surcharge = 45
else:
    amount = 130 + 162.50 + ((units - 50) * 8.45)
    surcharge = 75
total = amount + surcharge
print(total)