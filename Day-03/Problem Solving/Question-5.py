#Biling System in Super Market

total_bill = 0

for i in range(1,6):
    print("Enter the price of item",i)
    price = int(input())
    total_bill += price

print("Total bill is",total_bill)