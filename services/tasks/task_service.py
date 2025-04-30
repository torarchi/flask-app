from models.task import Task
from extensions import db
from flask_jwt_extended import get_jwt_identity

def create_task(data):
    user_id = get_jwt_identity()
    task = Task(title=data['title'], description=data.get('description'), user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    user_id = get_jwt_identity()
    return Task.query.filter_by(user_id=user_id).all()

def get_task(task_id):
    user_id = get_jwt_identity()
    return Task.query.filter_by(id=task_id, user_id=user_id).first()

def update_task(task_id, data):
    task = get_task(task_id)
    if task:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.is_completed = data.get('is_completed', task.is_completed)
        db.session.commit()
    return task

def delete_task(task_id):
    task = get_task(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return task

