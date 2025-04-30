from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.tasks import task_service

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@task_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    """
    Создание новой задачи
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    parameters:
      - in: body
        name: body
        schema:
          required:
            - title
          properties:
            title:
              type: string
              example: Купить продукты
            description:
              type: string
              example: Молоко, хлеб, сыр
    responses:
      201:
        description: Задача успешно создана
      400:
        description: Ошибка валидации
    """
    task = task_service.create_task(request.json)
    return jsonify(id=task.id, title=task.title), 201


@task_bp.route('/', methods=['GET'])
@jwt_required()
def read_all():
    """
    Получение всех задач пользователя
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    responses:
      200:
        description: Список задач
    """
    tasks = task_service.get_all_tasks()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'is_completed': t.is_completed
    } for t in tasks])


@task_bp.route('/<int:task_id>', methods=['GET'])
@jwt_required()
def read_one(task_id):
    """
    Получение задачи по ID
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
    responses:
      200:
        description: Задача найдена
      404:
        description: Задача не найдена
    """
    task = task_service.get_task(task_id)
    if not task:
        return jsonify({'msg': 'Task not found'}), 404
    return jsonify(id=task.id, title=task.title, description=task.description, is_completed=task.is_completed)


@task_bp.route('/<int:task_id>', methods=['PUT'])
@jwt_required()
def update(task_id):
    """
    Обновление задачи
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          properties:
            title:
              type: string
              example: Обновлённое название
            description:
              type: string
              example: Новое описание
            is_completed:
              type: boolean
              example: true
    responses:
      200:
        description: Задача обновлена
      404:
        description: Задача не найдена
    """
    task = task_service.update_task(task_id, request.json)
    if not task:
        return jsonify({'msg': 'Task not found'}), 404
    return jsonify({'msg': 'Task updated'})


@task_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete(task_id):
    """
    Удаление задачи
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
    responses:
      200:
        description: Задача удалена
      404:
        description: Задача не найдена
    """
    task = task_service.delete_task(task_id)
    if not task:
        return jsonify({'msg': 'Task not found'}), 404
    return jsonify({'msg': 'Task deleted'})

