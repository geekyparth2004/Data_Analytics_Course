#WAP to print the list in which the numbers are squared of numbers from 1 to 30 in function 

def numbers():
    a = []
    for i in range(1,31):
        val = i ** 2
        a.append(val)

    print(a)



numbers()