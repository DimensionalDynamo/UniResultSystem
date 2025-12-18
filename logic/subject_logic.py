import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from database.db_connection import get_db_connection
    print("Import successful!")
except ImportError as e:
    print(f"Still failing to import: {e}")
    sys.exit()

def add_subject(subject_name, subject_code, semester):
    connection = get_db_connection()
    cursor = None
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO subjects (subject_name, subject_code, semester) VALUES (%s, %s, %s)"
            values = (subject_name, subject_code, semester)
            
            cursor.execute(query, values)
            connection.commit()
            print("Subject added successfully.")
            return cursor.lastrowid
        except Exception as e:
            print(f"Error adding subject: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        print("Database connection failed.")
        return None

if __name__ == "__main__":
    print("Adding a new subject...")
    new_subject_id = add_subject("Data Structures", "CS201", 3)     
    if new_subject_id:
        print(f"New Subject ID: {new_subject_id}")
    else:
        print("Failed to add new subject.")