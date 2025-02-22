import psycopg2
from psycopg2 import sql, OperationalError
import psycopg2.extras

import os
from dotenv import load_dotenv
load_dotenv()

conn = None

# Function to connect to the database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')
        )
        print("Connection to PostgreSQL DB successful")
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None
   # finally:
       # if conn is not None:
           # conn.close()
#conn = get_db_connection()
def insert_news_data(news_df):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Insert rows into the table
            for _, row in news_df.iterrows():
                cursor.execute(
                    """
                    INSERT INTO news (timestamp, author, sentiment_score, description)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (row['timestamp'], row['author'], row['sentiment_score'], row['description'])
                )
            conn.commit()
            cursor.close()
            print("News data inserted successfully.")
        except Exception as e:
            print(f"Error inserting news data: {e}")
        finally:
            conn.close()
