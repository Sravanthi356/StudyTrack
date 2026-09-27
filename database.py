import sqlite3
def connect_db():
    connection = sqlite3.connect("studytrack.db")
    return connection

def create_table():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            priority TEXT NOT NULL,
            deadline TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_task_to_db(title, subject, priority, deadline, status):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, subject, priority, deadline, status)
        VALUES (?, ?, ?, ?, ?)
    """, (title, subject, priority, deadline, status))

    connection.commit()
    connection.close()

def get_tasks():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    return tasks

def update_task_in_db(task_id, status):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (status, task_id))
    connection.commit()
    connection.close()

def delete_task_from_db(task_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()

create_table()

