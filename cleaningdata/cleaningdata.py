
import pandas as pd 

#read the CSV file
df=pd.read_csv("bank.csv")


#drop colums
df=df.drop(columns=["RowNumber","Tenure", "Exited"])

#drop all the missing values/letter
condition = df['Surname'].str.isalpha()
df = df.loc[condition]

#save dataframe to csv file
df.to_csv("cleaned_bank.csv", index=False)