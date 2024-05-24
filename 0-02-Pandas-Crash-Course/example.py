import pandas as pd

df = pd.read_csv('salaries.csv')
print(df)

print(df['Salary'].mean())
print(df.Age)
