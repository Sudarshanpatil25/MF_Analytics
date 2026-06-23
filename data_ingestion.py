import pandas as pd
import os
from sqlalchemy import create_engine

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):

        file_path = os.path.join(folder, file)

        df = pd.read_csv(file_path)

        print("\n" + "="*50)
        print("FILE:", file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        engine = create_engine("sqlite:///data/mf_analytics.db")

for file in os.listdir(folder):
    if file.endswith(".csv"):
        file_path = os.path.join(folder, file)
        df = pd.read_csv(file_path)
        table_name = file.replace(".csv", "")
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Loaded {file} → {table_name}")

print("\n✅ All CSVs loaded to SQLite!")