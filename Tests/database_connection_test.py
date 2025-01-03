import os
import psycopg2


def test_db_connection():
    try:
        # Получаем параметры подключения из переменных окружения
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')

        # Устанавливаем соединение с базой данных
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Подключение к базе данных успешно!")
        connection.close()
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")


test_db_connection()
