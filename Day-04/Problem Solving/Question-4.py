a = float(input("Enter the number: "))
b = float(input("Enter the number: "))

print("Choose the operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter the choice: "))

if choice == 1:
    print("The sum of two numbers is: ", a+b)

elif choice == 2:
    print("The difference of two numbers is: ", a-b)

elif choice == 3:
    print("The product of two numbers is: ", a*b)
    
elif choice == 4:
    print("The division of two numbers is: ", a/b)
    
else: 
    print("Invalid choice")