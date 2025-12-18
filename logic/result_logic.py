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

def add_result(student_id, subject_id, marks_obtained):
    connection = get_db_connection()
    cursor = None

    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO results (student_id, subject_id, marks_obtained) VALUES (%s, %s, %s)"
            values = (student_id, subject_id, marks_obtained)
            
            cursor.execute(query, values)
            connection.commit()
            print(f"Result added: Student {student_id} got {marks_obtained} in Subject {subject_id}.")
            return cursor.lastrowid
            
        except Exception as e:
            print(f"Error adding result: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        print("Database connection failed.")
        return None

if __name__ == "__main__":
    print("Adding a new result...")
    
    student_id = 1  
    subject_id = 1
    marks = 85
    
    result_id = add_result(student_id, subject_id, marks)
    
    if result_id:
        print(f"New Result ID: {result_id}")
    else:
        print("Failed to add result.")