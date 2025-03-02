import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')

# printng the duplicate rows
print("printng the duplicate rows \n",df[df.duplicated()])

#removing duplicate rows
df.drop_duplicates(inplace=True)

# printing after removing duplicates
print("printing after removing duplicates \n",df)

# after removing duplicate rows checking presence of any duplicate rows further
print("after removing duplicate rows checking presence of any duplicate rows further \n",df.duplicated())

# writing to the file
df.to_csv('data.csv',index=False)