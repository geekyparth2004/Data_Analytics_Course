import addition
import subtraction
import multiplication
import division

print("Press 1 - Addition")
print("Pess 2 - Substraction")
print("Press 3 - Multiplication")
print("Press 4 - Divison")
c = int(input("Enter the number:"))

        
def calculator(x,y,c):
    if(c==1): return addition.add(x,y)
    elif(c==2): return subtraction.diff(x,y)
    elif(c==3): return multiplication.mul(x,y)
    elif(c==4): return division.div(x,y)
    else : return "Invalid Value"
    

x = int(input("Enter the first value : "))
y = int(input("Enter the second value : "))

print("Your answer is :",calculator(x,y,c))