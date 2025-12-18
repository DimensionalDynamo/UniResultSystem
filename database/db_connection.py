import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='university_results'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

if __name__ == "__main__":
    print("Testing database connection...")
    conn = get_db_connection()
    if conn:
        print("Database connection established.")
        conn.close()
    else:
        print("Failed to connect to the database.")