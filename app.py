import db
from tasksDAO import TasksDAO
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Define route to display tasks
@app.route('/')
def index():
    table = DAO.retrieve_all()
    return render_template('index.html', table=table)

# Define route for task insertion
@app.route('/add_task', methods=['POST'])
def add_task():
    taskID = request.form['taskID']
    taskDescription = request.form['taskDescription']
    dueDate = request.form['dueDate']
    
    DAO.insert_task(taskID, taskDescription, dueDate)

    return redirect('/')

# Define route for task update
@app.route('/update_task', methods=['POST'])
def update_task():
    taskID = request.form['taskID']
    taskDescription = request.form['taskDescription']
    dueDate = request.form['dueDate']
    completionStatus = request.form['completionStatus']
    
    DAO.update_task(taskID, taskDescription, dueDate, completionStatus)

    return redirect('/')

# Define route for task deletion
@app.route('/delete_task', methods=['POST'])
def delete_task():
    taskID = request.form['taskID']

    DAO.delete_task(taskID)
    
    return redirect('/')

if __name__ == '__main__':
    DAO = TasksDAO()
    app.run(debug=True)
    # DAO.insert_task()
    table = DAO.retrieve_all()
    # Process the rows
    for row in table:
        print(row)

    # Close cursor and connection
    TasksDAO.cursor.close()
    db.connection.close()