import pyodbc
import requests

# הגדרות חיבור ל-SQL Server
# שים לב: אם ה-SQL שלך דורש משתמש וסיסמה, שנה את ה-Connection String
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;' 
    r'DATABASE=Northwind;'
    r'Trusted_Connection=yes;'
)

def run_ddt_test():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # שליפת נתונים מה-Northwind - למשל רשימת קטגוריות
        cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
        rows = cursor.fetchall()

        for row in rows:
            cat_id = row.CategoryID
            expected_name = row.CategoryName
            
            # כאן אתה קורא ל-API (נשתמש ב-URL לדוגמה, שנה ל-URL של המשימה שלך)
            api_url = f"https://api.example.com/categories/{cat_id}"
            response = requests.get(api_url)
            
            if response.status_code == 200:
                print(f"Testing ID {cat_id}: Success!")
            else:
                print(f"Testing ID {cat_id}: Failed with status {response.status_code}")

        conn.close()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_ddt_test()
    print("Run ddt from sql server")