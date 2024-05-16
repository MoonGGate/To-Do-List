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
    var errorLabel = document.createElement('label');
    errorLabel.textContent = errorMessage;
    errorLabel.style.color = 'red';

    var inputElement = document.getElementById(inputID);
    inputElement.insertAdjacentElement('afterend', errorLabel);
}

document.getElementById('addTaskForm').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get form input values
    var taskID = document.getElementById('taskID').value.trim();

    // Validate ID
    if (!taskID) {
        displayError('taskID', 'Task ID is required');
        return;
    } else if (isNaN(taskID)) {
        displayError('taskID', 'Task ID can only contain numbers from 0-9');
        return;
    } else {
        // Check if ID exists asynchronously
        checkIfIdExists(taskID)
            .then(idExists => {
                if (idExists) {
                    displayError('taskID', 'Task ID already exists');
                    console.log('Task ID already exists');
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

