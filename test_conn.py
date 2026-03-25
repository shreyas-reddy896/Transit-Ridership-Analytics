import pandas as pd
from sqlalchemy import create_engine

# 🔹 Load your CSV
df = pd.read_csv("cta_ridership_data.csv")

print(df.head())  # sanity check

# 🔹 Create connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Hask5470@database-ctaridership.c47ig0mgw5kq.us-east-1.rds.amazonaws.com:5432/postgres"
)

# 🔹 Upload to RDS
df.to_sql("ridership", engine, if_exists="replace", index=False)

print("Data uploaded successfully 🚀")