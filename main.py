import db
import tasksDAO

if __name__ == '__main__':
    DAO = tasksDAO.TasksDAO()

    table = DAO.retrieve_all()
    # Process the rows
    for row in table:
        print(row)

    # Close cursor and connection
    DAO.cursor.close()
    db.connection.close()