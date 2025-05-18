import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv(r"C:\Users\Palak\OneDrive\Documents\hotel_bookings.csv")

print(df)
print(df.head(20))
host = "localhost"
user = "root"
password = "nikh1603"
database = "ankit"
table_name = "hbooks"
port = "3306"



engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')



(df.head(20)).to_sql(name=table_name,if_exists="replace",con=engine,index=False)
print("Data exported successfully!")
