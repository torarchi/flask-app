from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Регистрация нового пользователя
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        schema:
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: user@example.com
            password:
              type: string
              example: secret123
    responses:
      201:
        description: Успешная регистрация
      400:
        description: Ошибка валидации
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user, error = AuthService.register(email, password)
    if error:
        return jsonify({'error': error}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Вход пользователя
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        schema:
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: user@example.com
            password:
              type: string
              example: secret123
    responses:
      200:
        description: Успешный вход
      401:
        description: Неверные данные
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    token, error = AuthService.login(email, password)
    if error:
        return jsonify({'error': error}), 401

    return jsonify({'access_token': token})

