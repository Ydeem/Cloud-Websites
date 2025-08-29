import pandas as pd

df=pd.read_csv('detail_report .csv')

file=pd.DataFrame(df)

print(file.head())