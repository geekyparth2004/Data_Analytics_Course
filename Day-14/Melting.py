import pandas as pd

dict = {"Fruits":["Mangoes","Banana","Apple","Grapes"],
        "Price":[100,50,150,30],
        "Quantity":[50,10,1,50]}

df = pd.DataFrame(dict)

print(df)

print(df.melt(id_vars=["Fruits"],value_vars=["Price"]))