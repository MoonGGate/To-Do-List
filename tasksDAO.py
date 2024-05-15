import db

class TasksDAO:
    def __init__(self) -> None:
        self.cursor = db.connection.cursor()

    def insert_task(self):
        taskID = input("Please enter task ID: ")
        taskDescription = input("Please enter task Description: ")
        dueDate = input("Please enter task due date: ")
        completionStatus = "Not Completed"
        query = f"INSERT INTO tasks VALUES ({taskID}, '{taskDescription}', '{dueDate}', '{completionStatus}');"
        self.cursor.execute(query)
        db.connection.commit()
        return print("Inserted a task successfully")

    # insert_task()     # Works

    def retrieve_task(self):
        taskID = input("Enter the task ID: ")
        query = f"SELECT * FROM tasks WHERE taskID = {taskID};"
        self.cursor.execute(query)
        return print(self.cursor.fetchone())

    # retrieve_task()     # Works

    def update_task(self):
        print("1: Update task ID\n2: Update task description\n3: Update task due date\n4: Update task completion status")
        update_option = input().strip()
        if update_option == "1":
            old_id = input("Which task ID would you like to change: ")
            new_id = input("What ID would you like to put instead: ")
            query = f"UPDATE tasks SET taskID = {new_id} WHERE taskID = {old_id};"
            self.cursor.execute(query)
            db.connection.commit()
            return print("Updated task ID successfully")
        elif update_option == "2":
            old_desc = input("Enter the task ID: ")
            new_desc = input("What task description would you like to put instead: ")
            query = f"UPDATE tasks SET taskDescription = '{new_desc}' WHERE taskID = {old_desc};"
            self.cursor.execute(query)
            db.connection.commit()
            return print("Updated task description successfully")
        elif update_option == "3":
            old_date = input("Enter the task ID: ")
            new_date = input("What task due date would you like to put instead: ")
            query = f"UPDATE tasks SET dueDate = '{new_date}' WHERE taskID = {old_date};"
            self.cursor.execute(query)
            db.connection.commit()
            return print("Updated task description successfully")
        elif update_option == "4":
            old_status = input("Enter the task ID: ")
            new_status = input("What completion status would you like to put instead: ")
            query = f"UPDATE tasks SET completionStatus = '{new_status}' WHERE taskID = {old_status};"
            self.cursor.execute(query)
            db.connection.commit()
            return print("Updated task description successfully")
        
    #update_task()   # Works

    def delete_task(self):
        taskID = input("Enter the task ID: ")
        query = f"DELETE FROM tasks WHERE taskID = {taskID};"
        self.cursor.execute(query)
        db.connection.commit()
        return print("The task has been deleted successfully")

    # delete_task()   # Works

    def retrieve_all(self):
        query = "SELECT * FROM tasks"
        self.cursor.execute(query)
        return self.cursor.fetchall()