x = 2
print(x)
def hello():
    global x
    x = 1
    return x

print(hello())
print(x)