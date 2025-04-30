# Стек технологий

Flask

Flask-SQLAlchemy – ORM

Flask-Bcrypt – хеширование паролей

Flask-JWT-Extended – авторизация по токену

Flasgger – Swagger-документация

SQLite – БД по умолчанию

# Архитектура

controllers/         # HTTP маршруты (Blueprint)

services/            # Бизнес-логика

models/              # Модели SQLAlchemy

extensions.py        # Инициализация расширений

app.py               # Точка входа

config.py            # Настройки

# Авторизация

При входе возвращается JWT access token

Токен создаётся по user.id

Токен используется в заголовке:

Authorization: Bearer <токен>

Токены можно использовать для защиты маршрутов с @jwt_required()

# Установка

git clone https://github.com/torarchi/flask-app

cd flask_auth_api

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

Создатся файл .env (его никуда не показываем, там все пароли приложения)
Внутри указываем из пункта снизу **env**

python app.py


# Важно

если устанавливаете новую библиотеку, что-бы она записалась в requirements.txt и ничего не сломалось прописывайте каждый раз после установки чего-либо

pip freeze > requirements.txt



# env

**Flask секрет (обязателен для безопасности, свой придумываем)**

SECRET_KEY=your-secret-key

**JWT-токены (подпись токенов тоже свой придумываем)**

JWT_SECRET_KEY=your-jwt-secret-key

**Подключение к БД:**
**SQLite (локально, по умолчанию sqlite)**

DATABASE_URL=sqlite:///app.db

**или MySQL (пример на будущее):**

DATABASE_URL=mysql+pymysql://root:password@localhost/mydb


# Swagger UI

Доступен по адресу:

http://localhost:5000/apidocs



# Как писать код

Контроллер — только получает запрос и вызывает сервис

Вся логика (валидация, сохранение, хеширование, токены) — в сервисах

Модели — только структура таблиц

Используй extensions.py, чтобы избежать циклических импортов


