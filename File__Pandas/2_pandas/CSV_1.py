

import pandas as pd

data = pd.read_csv("push.csv")

df = pd.DataFrame(data)
print(df)

print("\n----------------------------------------------\n")

des = df.describe()
print(des)

print("\n----------------------------------------------\n")

infor = df.info()
print(infor)