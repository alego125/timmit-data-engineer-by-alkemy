import sqlite3
import logging
import pandas as pd
from pathlib import Path

# Logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    datefmt="%Y-%m-%dY%H:%M:%S%z")

# Root path of module folder to will be use into db connections
rootPath = Path(__file__).parent.parent

try:
    # Get and read csv
    url = 'http://winterolympicsmedals.com/medals.csv'
    dfMedals = pd.read_csv(url)
except Exception as ex:
    logging.error(f"Error - we cant't read csc file {ex}")

try:
    # Create Database connection and cursor
    conn = sqlite3.connect(f"{rootPath}/src/olympics.db")
    cursor = conn.cursor()
except sqlite3.OperationalError as ex:
    logging.error(f"Error into sqlite connection {ex}")

# Filter dataframe by Medal, NOC and year
dfFiltered = dfMedals[
    (dfMedals['Medal'] == 'Gold') &
    (dfMedals['NOC'] == 'USA') &
    (dfMedals['Year'] >= 1950)
    ]

# Query to create table and cursor
query = """CREATE TABLE IF NOT EXISTS medals (
            id INTEGER,
            year INTEGER,
            city TEXT,
            sport TEXT,
            discipline TEXT,
            noc TEXT,
            event TEXT,
            event_gender TEXT,
            medal TEXT
            )"""

try:

    # Excecute, then commit and at the end close connection to database
    cursor.execute(query)
    conn.commit()
    logging.info("Query excecuted successfuly")   
except Exception as ex:
    logging.error(f"Error in query excecution {ex}")

try:
    # Insert data into database using to_sql pandas method
    dfFiltered.to_sql(name='orders', con=conn, if_exists='append', index = False)
except Exception as ex:
    logging.error(f"Error with creation query to sql {ex}")

# Verify register in database with a simple select query
query = "SELECT * FROM orders"
data = pd.read_sql(query, con=conn)
print(data)

# Finally close connection
conn.close()
