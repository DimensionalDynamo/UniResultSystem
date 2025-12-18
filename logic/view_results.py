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

# REMOVED 'student_id' from the brackets below so it matches the call at the bottom
def view_all_results():
    connection = get_db_connection()
    cursor = None

    if connection:
        try:
            cursor = connection.cursor()
            
            # This query joins all 3 tables to give a complete report
            query = """
            SELECT 
                students.student_name, 
                students.roll_number, 
                subjects.subject_name, 
                results.marks_obtained 
            FROM results
            JOIN students ON results.student_id = students.student_id
            JOIN subjects ON results.subject_id = subjects.subject_id
            """
            
            cursor.execute(query)
            records = cursor.fetchall()
            
            print("\n" + "="*70)
            print(" UNIVERSITY RESULT REPORT ")
            print("="*70)
            
            if records:
                # Print Table Header
                print(f"{'Name':<20} | {'Roll No':<15} | {'Subject':<20} | {'Marks':<5}")
                print("-" * 70)
                
                for row in records:
                    name, roll, subject, marks = row
                    print(f"{name:<20} | {roll:<15} | {subject:<20} | {marks:<5}")
                print("-" * 70)
            else:
                print("\nNo results found in the database.")
            
        except Exception as e:
            print(f"Error fetching results: {e}")
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        print("Database connection failed.")

if __name__ == "__main__":
    view_all_results()