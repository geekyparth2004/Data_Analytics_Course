#WAP to find sum of all even numbers upto 50 

sum = 0
for i in range(1,51):
    if(i%2==0):
        sum += i
print(sum)
