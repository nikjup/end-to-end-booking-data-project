import pandas as pd
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="nikh1603",database="ankit")
query=" select * from hbooks left join hpricing on hbooks.hotel=hpricing.`Hotel name` union  select * from hbooks right join hpricing on hbooks.hotel=hpricing.`Hotel name`;"
df=pd.read_sql(query,conn)
print(df)
print(df[df.duplicated()])
df[df.duplicated(subset=['hotel', 'arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'])]
print(df.isnull().sum())
#print(df.dropna(inplace=True))
#print(df)
df[df.select_dtypes(include='object').columns] = df.select_dtypes(include='object').fillna("Unknown")
df[df.select_dtypes(include="number").columns]=df.select_dtypes(include="number").fillna(0)
#print(df.fillna("Unknown", inplace=True))
print(df)
for col in df.select_dtypes(include='object').columns:
    if df[col].str.contains(r'^\s+|\s+$', regex=True).any():
        print(f"Whitespace issue in: {col}")
#for col in df.select_dtypes(include='number').columns:
    #if df[col].str.contains(r'^\s+|\s+$', regex=True).any():
       # print(f"Whitespace issue in: {col}")
df[df.select_dtypes(include='object').columns] = df[df.select_dtypes(include='object').columns].apply(lambda x: x.str.strip().str.title())
#df[df.select_dtypes(include='number').columns] = df[df.select_dtypes(include='number').columns].apply(lambda x: x.int.strip().int.title())
print(df.dtypes)
df=df.convert_dtypes()
print(df.dtypes)
print(df.describe())
df.reset_index(drop=True, inplace=True)
print(df)


df.to_excel("barcelona.xlsx",index=False,engine="openpyxl")
print("shared successfully")
