import pandas as pd
#a csv file dataset that we have already took
df=pd.read_csv("Housing1.csv")
#Converting to excel sheet
df.to_excel("Housing.xlsx",index=False)
