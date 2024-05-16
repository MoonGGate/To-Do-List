import db

class TasksDAO:
    # Initializes a cursor
    def __init__(self) -> None:
        self.cursor = db.connection.cursor()

    def insert_task(self, taskID, taskDescription, dueDate):
        completionStatus = "Not Completed"
        query = "INSERT INTO tasks VALUES (%s, %s, %s, %s);"
        values = (taskID, taskDescription, dueDate, completionStatus)
        try:
            self.cursor.execute(query, values)
            db.connection.commit()
            return print("Inserted a task successfully")
        except Exception as e:
            # Handle the exception (e.g., log the error, return an error message)
            return print(f"Error inserting task: {str(e)}")

    def retrieve_task(self, taskID):
        query = f"SELECT * FROM tasks WHERE taskID = {taskID};"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as e:
            # Handle the exception (e.g., log the error, return an error message)
            return print(f"Error retrieving task: {str(e)}")

    def update_task(self, taskID, taskDescription = None, dueDate = None, completionStatus = "Not completed"):
        query = "UPDATE tasks SET "
        updates = []

        if taskDescription is not "":
            updates.append(f"taskDescription = '{taskDescription}'")
        if dueDate is not "":
            updates.append(f"dueDate = '{dueDate}'")
        if completionStatus is not "Not completed":
            updates.append(f"completionStatus = '{completionStatus}'")

        if updates:
            query += ", ".join(updates) 
            query += f"WHERE taskID = {taskID};"

        try:
            self.cursor.execute(query)
            db.connection.commit()
            return print("Updated a task successfully")
        except Exception as e:
            # Handle the exception (e.g., log the error, return an error message)
            return print(f"Error retrieving task: {str(e)}")
        
    def delete_task(self, taskID):
        query = f"DELETE FROM tasks WHERE taskID = {taskID};"
        try:
            self.cursor.execute(query)
            db.connection.commit()
            return print("The task has been deleted successfully")
        except Exception as e:
            # Handle the exception (e.g., log the error, return an error message)
            return print(f"Error retrieving task: {str(e)}")

    def retrieve_all(self):
        query = "SELECT * FROM tasks;"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            # Handle the exception (e.g., log the error, return an error message)
            return print(f"Error retrieving task: {str(e)}")
    
    # Error Handling
    def check_id_exists(self, taskID):
        query = "SELECT taskID FROM tasks;"
        self.cursor.execute(query)
        ids = self.cursor.fetchall()
        for id in ids:
            if taskID == id[0]:
                return 'true'   # Returns string because its later passed to script.js
        return 'false'


test = TasksDAO()
print(test.check_id_exists(1))