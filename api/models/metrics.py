import mysql.connector

def save_metric(service, status, response_time):
    conn = mysql.connector.connect(
        host="db",
        user="user",
        password="pass",
        database="app"
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO metrics (service, status, response_time) VALUES (%s, %s, %s)",
        (service, status, response_time)
    )

    conn.commit()
    cursor.close()
    conn.close()