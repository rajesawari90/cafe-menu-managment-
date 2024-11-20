import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Replace with your database connection details
engine = create_engine('mysql+pymysql://new_user:password123@localhost/mydatabase')

# Query the database
query = "SELECT * FROM my_table"
df = pd.read_sql(query, engine)
print(df)
# Export to Excel
df.to_excel('output.xlsx', index=False)


