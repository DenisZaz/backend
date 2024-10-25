# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install flask

# Копируем код приложения
COPY app.py /app/app.py

# Создаем директорию для сохранения data.txt
RUN mkdir -p /app/data
VOLUME /app/data

# Переходим в рабочую директорию
WORKDIR /app

# Устанавливаем переменные окружения для Flask
ENV FLASK_APP=app.py

# Запускаем Flask-сервер на 8000 порту
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]