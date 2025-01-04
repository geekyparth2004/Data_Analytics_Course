b = [13,7,12,10]

# WAP to multiply all the numbers in the list

mul = 1

for i in range(0,len(b)): 
    mul *= b[i]

print(mul)



# WAP to get the largest number from the list

b.sort()

print(b[-1])


# WAP to get the smallest number in the list

print(b[0])
