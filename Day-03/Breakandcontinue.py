#Break statemenet is used to destory the entire loop and pointer comes out of the loop 
#Continue statement is used to skip the current iteration and move to the next iteration

# Example of Break Statement

for i in range(1,11):
    if(i==5):
        break
    else: print (i)
    
    
# Example of Continue Statement

for i in range(1,11):
    if(i==5):
        continue
    else: print (i)
