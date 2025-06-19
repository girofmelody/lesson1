from sqlalchemy import create_engine

# Строка подключения к базе данных
db_url = 'postgresql://postgres:1234@localhost:5432/postgres'

# Создание объекта engine
try:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        print("успешное подключение к БД")
except Exception as e:
    print("ошибка подключения:", e)