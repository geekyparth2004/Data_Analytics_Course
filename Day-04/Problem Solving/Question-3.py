
a = int(input("Enter the number"))
original = a
rev = 0 
while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10
    
if(original==rev):
    print("The number is palindrome")
    
else:
    print("The number is not palindrome")