import mysql.connector
import os

def check_db():
    """Verifica se o banco MySQL está acessível"""
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "db"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASS", "root"),
            database=os.environ.get("DB_NAME", "monitor")
        )
        conn.close()
        return True
    except Exception as e:
        print(f"❌ DB ERROR: {e}")
        return False