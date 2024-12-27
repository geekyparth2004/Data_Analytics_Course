#WAP check wheather the given number is 2 digit upto 5 digit

a = int(input("Enter the number"))

while(a>0):
    if(a>9 and a<100):
        print("The given number is 2 digit")
        break
    elif(a>99 and a<1000):
        print("The given number is 3 digit")
        break
    elif(a>999 and a<10000):
        print("The given number is 4 digit")
        break
    elif(a>9999 and a<100000):
        print("The given number is 5 digit")
        break
    else:
        print("The given number is not in the range")
        break
    