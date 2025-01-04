a = ["Khushboo","Parth","Rahul","Naman","Riya","Parth","Khushboo"]

# To find the length of the list

print(len(a))

# To find the occurence of the particular value in the list 

print(a.count("Parth"))

# To add on the list

a.append("Riya")
print(a)

# To insert at any particular location 

a.insert(1,"Plant")
print(a)


# To remove from the list

a.remove("Plant")
print(a)

# To remove from a certain location

print(a.pop(2))
print(a)