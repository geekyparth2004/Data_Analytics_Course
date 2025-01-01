a = {"Name":"Parth Goel","Age":23}

# Get function 

print(a.get("Name"))

# Item function 

val = a.items()
for i in val:
    print(i)

# Values print
c = a.values()

for i in c:
    print(i)

# Keys 

d = a.keys()

for i in d:
    print(i)
    
# Copy Function 

e = a.copy()

print(e)

