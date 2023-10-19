import pandas as pd 

#read the CSV file
df=pd.read_csv("bank.csv")


#drop colums
df=df.drop(columns=["RowNumber","Tenure", "Exited"])

#save dataframe to csv file
df.to_csv("cleaned_bank.csv", index=False)
