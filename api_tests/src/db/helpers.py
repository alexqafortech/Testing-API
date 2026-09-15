class DBHelper:

    def __init__(self, connection):
        self.conn = connection

    def get_user_by_email(self, email: str) -> dict | None:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, email, username, is_active FROM users WHERE email = %s",
            (email,)
        )
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return {"id": row[0], "email": row[1], "username": row[2], "is_active": row[3]}

    def get_task_by_id(self, task_id: str) -> dict | None:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, title, status, priority, user_id FROM tasks WHERE id = %s",
            (task_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return {"id": row[0], "title": row[1], "status": row[2], "priority": row[3], "user_id": row[4]}

    def count_tasks_by_user(self, user_id: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) from tasks where user_id = %s", (user_id,))
        count = cursor.fetchone()[0]
        cursor.close()
        return count