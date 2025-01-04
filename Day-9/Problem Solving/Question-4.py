a = [1,2,3,4,5,5,6,7,8,0]

def sum():
    val = 0
    for i in range(0,len(a)):
        val += a[i]
    print(val)

sum()
