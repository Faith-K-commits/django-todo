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

// Function to handle task completion (this can be expanded to include API calls)
document.querySelectorAll('.task-done input').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const taskItem = this.closest('.task-item');
        if (this.checked) {
            taskItem.classList.add('done');
        } else {
            taskItem.classList.remove('done');
        }
    });
});

