from flask import Blueprint, render_template, request, redirect, url_for
from database.mongo import get_tasks, add_task, update_task, delete_task

# Create a Blueprint for tasks
tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def index():
    tasks = get_tasks()  # Retrieve tasks from the database
    return render_template('index.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add_task_route():
    task_content = request.form.get('content')
    if task_content:
        add_task(task_content)  # Add task to the database
    return redirect(url_for('tasks.index'))

@tasks_bp.route('/update/<task_id>', methods=['POST'])
def update_task_route(task_id):
    # Check if the completed checkbox was checked
    completed = 'completed' in request.form
    update_task(task_id, completed)  # Update task in the database
    return redirect(url_for('tasks.index'))

@tasks_bp.route('/delete/<task_id>', methods=['POST'])
def delete_task_route(task_id):
    delete_task(task_id)  # Delete task from the database
    return redirect(url_for('tasks.index'))
