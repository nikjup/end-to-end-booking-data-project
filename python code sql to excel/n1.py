import pandas as pd
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="nikh1603",database="ankit")
query="select * from hreviews left join hpricing on hreviews.city=hpricing.city union select * from hreviews right join hpricing on hreviews.city=hpricing.city;"
df=pd.read_sql(query,conn)
print(df.head(5))
print(df)
print(df[df.duplicated()])
print(df.isnull().sum())
df[df.select_dtypes(include='object').columns] = df.select_dtypes(include='object').fillna("Unknown")
df[df.select_dtypes(include="number").columns]=df.select_dtypes(include="number").fillna(0)
print(df)
for col in df.select_dtypes(include='object').columns:
    if df[col].str.contains(r'^\s+|\s+$', regex=True).any():
        print(f"Whitespace issue in: {col}")
df[df.select_dtypes(include='object').columns] = df[df.select_dtypes(include='object').columns].apply(lambda x: x.str.strip().str.title())
print(df.dtypes)
df=df.convert_dtypes()
print(df.dtypes)
print(df.describe())
df.reset_index(drop=True, inplace=True)
print(df)
df.to_excel("intel.xlsx",index=False,engine="openpyxl")
print("sent successfully")

