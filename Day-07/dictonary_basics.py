a = {"Name":"Parth Goel","Age":23}

print(a["Name"])

# Iteration in dictonary 

# Print all the keys one by one

for i in a:
    print(i)

# To print all the values one by one 

for i in a:
    print(a[i])
    
    
# Using value function 

for i in a.values():
    print(i)
    
# Using item function 

for i,j in a.items():
    print(i,j)