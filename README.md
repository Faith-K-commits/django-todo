# Django Todo Application

## Overview
This Django ToDo application allows users to manage their tasks efficiently. It includes features such as user registration, login, and CRUD operations (Create, Read, Update, Delete) on tasks. The application is responsive, providing an optimal experience across devices, and includes functionality to hide completed tasks from the task list.

# Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

# Features
- User Authentication: Secure user registration and login functionalities.
- Task Management: Users can create, read, update and delete tasks.
- Responsive Design: The application is fully responsive, ensuring it works seamlessly on desktops, tablets, and mobile devices.
- Hide Completed Tasks: Users can hide completed tasks from the task list to focus on pending tasks.

# Technologies Used
- Backend: Django 
- Frontend: HTML5, CSS3, JavaScript 
- Database: SQLite 
- Deployment: Heroku

# Prerequisites
- Python 
- Django 
- pip 
- Virtualenv 

# Installation
1. Clone the repository
    ```bash
        git clone https://github.com/Faith-K-commits/django-todo.git
        cd django-todo
    ```
2. Create and activate a virtual environment
    ```bash
        python3 -m venv venv
        source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```
3. Install the dependencies
   ```bash
      pip install -r requirements.txt
   ```
4. Run migrations
   ```bash
      python manage.py migrate
   ```
5. Create superuser
   ```bash
      python manage.py createsuperuser
   ```
6. Run the development server
   ```bash
      python manage.py runserver
   ```
7. Access the application
   Open your web browser and go to http://127.0.0.1:8000/

# Usage
## User Authentication
- Register: Visit `/register/` to create a new account.
- Login: Visit `/login/` to access your account.

## Task Management
- Create Task: Use the `plus` button on the tasks list to add a new task.
- View Tasks: All tasks are listed on the homepage.
- Edit Task: Click the `Edit` button next to a task to update it.
- Delete Task: Click the `Delete` button to remove a task.
- Mark Tasks as Complete: Click the `checkbox` to mark tasks as complete.
- Hide Completed Tasks: Use the `Hide Completed` toggle to filter out tasks that are marked as completed.