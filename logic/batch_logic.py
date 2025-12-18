import sys
import os
from datetime import date

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

print(f"Project Root found at: {parent_dir}")

try:
    from database.db_connection import get_db_connection
    print("Import successful!")
except ImportError as e:
    print(f"Still failing to import: {e}")
    sys.exit()

def add_batch(batch_name, start_date, end_date):
    connection = get_db_connection()
    cursor = None  # 1. Initialize cursor to None for safety

    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO batches (batch_name, start_date, end_date) VALUES (%s, %s, %s)"
            values = (batch_name, start_date, end_date)
            
            cursor.execute(query, values)
            connection.commit()
            print("Batch added successfully.")
            return cursor.lastrowid
            
        except Exception as e:
            print(f"Error adding batch: {e}")
            return None
        finally:
            # 2. Only close if cursor exists
            if cursor:
                cursor.close()
            connection.close()
    else:
        # 3. Explicit error if connection fails
        print("Failed to connect to the database.")
        return None

if __name__ == "__main__":
    print("Adding a new batch...")
    # This adds a batch named "2024 Spring"
    batch_id = add_batch("2024 Spring", date(2024, 1, 10), date(2024, 5, 15))
    
    if batch_id:
        print(f"New batch ID: {batch_id}")
    else:
        print("Failed to add new batch.")