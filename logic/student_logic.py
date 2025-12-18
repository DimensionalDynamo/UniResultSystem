import sys
import os
from datetime import date 

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from database.db_connection import get_db_connection
    print("Import successful!")
except ImportError as e:
    print(f"Still failing to import: {e}")
    sys.exit()

def add_student(student_name, roll_number, batch_id):
    connection = get_db_connection()
    cursor = None
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO students (student_name, roll_number, batch_id) VALUES (%s, %s, %s)"
            values = (student_name, roll_number, batch_id)
            
            cursor.execute(query, values)
            connection.commit()
            print("Student added successfully.")
            return cursor.lastrowid
        except Exception as e:
            print(f"Error adding student: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        print("Database connection failed.")
        return None

if __name__ == "__main__":
    print("Adding a new student...")
    new_student_id = add_student("Aditya", "BCA/2023/001", 1)     
    if new_student_id:
        print(f"New Student ID: {new_student_id}")
    else:
        print("Failed to add new student.")