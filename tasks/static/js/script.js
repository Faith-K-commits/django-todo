document.addEventListener("DOMContentLoaded",()=> {
    console.log('JavaScript file is loaded');

// Hide or show completed tasks based on the checkbox
document.querySelector('.hide-done-tasks input').addEventListener('change', function() {
    const tasks = document.querySelectorAll('.task-item');
    tasks.forEach(task => {
        if (this.checked && task.classList.contains('done')) {
            task.style.display = 'none';
        } else {
            task.style.display = 'block';
        }
    });
});

// Function to handle task completion
document.querySelectorAll('.task-done input').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const taskItem = this.closest('.task-item');
        const taskId = taskItem.getAttribute('data-task-id');
        const completed = this.checked;

        fetch(`/complete_task/${taskId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `completed=${completed}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                if (completed) {
                    taskItem.classList.add('done');
                } else {
                    taskItem.classList.remove('done');
                }
            } else {
                alert('Failed to update task status.');
            }
        });
    });
});
})