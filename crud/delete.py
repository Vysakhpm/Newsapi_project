from db import get_db_connection

def delete_user(id, timestamp,  author, sentiment_score, description):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM news WHERE id = %s;"
            cursor.execute(query, (id, timestamp,  author, sentiment_score, description))
            conn.commit()
            cursor.close()
            print(f"User: {id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            conn.close()