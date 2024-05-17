// Error Handling
function checkIfIdExists(taskID) {
    return fetch('/check_id/' + taskID)
        .then(response => response.text()) 
        .then(idExists => {
            if (idExists == 'true') {
                return true;
            } else {
                return false;
            }
        })
        .catch(error => {
            console.log('Error checking ID:', error);
        });
}

function displayError(inputID, errorMessage) {
    let errorLabel = document.createElement('label');
    errorLabel.textContent = errorMessage;
    errorLabel.style.color = 'red';

    let inputElement = document.getElementById(inputID);
    inputElement.insertAdjacentElement('afterend', errorLabel);
}

// ID check for addTaskForm
document.getElementById('addTaskForm').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get form input values
    let taskID = document.getElementById('addTaskID').value.trim();

    // Validate ID
    if (!taskID) {
        displayError('addTaskID', 'Task ID is required');
        return;
    } else if (isNaN(taskID)) {
        displayError('addTaskID', 'Task ID can only contain numbers from 0-9');
        return;
    } else {
        // Check if ID exists asynchronously
        checkIfIdExists(taskID)
            .then(idExists => {
                if (idExists) {
                    displayError('addTaskID', 'Task ID already exists');
                } else {
                    // Proceed with form submission if ID does not exist
                    event.target.submit();
                }
            })
            .catch(error => {
                console.error('Error checking ID:', error);
            });
    }
});

// ID check for updateTaskForm
document.getElementById('updateTaskForm').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get form input values
    let taskID = document.getElementById('updateTaskID').value.trim();

    // Validate ID
    if (!taskID) {
        displayError('updateTaskID', 'Task ID is required');
        return;
    } else if (isNaN(taskID)) {
        displayError('updateTaskID', 'Task ID can only contain numbers from 0-9');
        return;
    } else {
        // Check if ID exists asynchronously
        checkIfIdExists(taskID)
            .then(idExists => {
                if (!idExists) {
                    displayError('updateTaskID', 'ID does not exist');
                } else {
                    // Proceed with form submission if ID does not exist
                    event.target.submit();
                }
            })
            .catch(error => {
                console.error('Error checking ID:', error);
            });
    }
});

// ID check for deleteTaskForm
document.getElementById('deleteTaskForm').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get form input values
    let taskID = document.getElementById('deleteTaskID').value.trim();

    // Validate ID
    if (!taskID) {
        displayError('deleteTaskID', 'Task ID is required');
        return;
    } else if (isNaN(taskID)) {
        displayError('deleteTaskID', 'Task ID can only contain numbers from 0-9');
        return;
    } else {
        // Check if ID exists asynchronously
        checkIfIdExists(taskID)
            .then(idExists => {
                if (!idExists) {
                    displayError('deleteTaskID', 'ID does not exist');
                } else {
                    // Proceed with form submission if ID does not exist
                    event.target.submit();
                }
            })
            .catch(error => {
                console.error('Error checking ID:', error);
            });
    }
});