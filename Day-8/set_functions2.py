a = {2,1,3,4,2,3,1}
b = {4,23,41,3,4,1}

# is disjoint 

print(a.isdisjoint(b))

# is subset 

print(a.issubset(b))

# is superset

print(b.issuperset(b))

# Update

a.update(b)

# Clear

b.clear()

print(b)

