import pandas as pd
from sqlalchemy import create_engine, inspect

# SQLite (текущая база)
sqlite_engine = create_engine("sqlite:///app.db")

# PostgreSQL (Docker)
pg_engine = create_engine("postgresql://user:password@postgres:5432/mydb")

# Получаем список таблиц SQLite
inspector = inspect(sqlite_engine)
tables = inspector.get_table_names()

print("Tables in SQLite:", tables)

# Перенос данных в PostgreSQL
for table in tables:
    print(f"Transferring table: {table}")

    # Читаем данные из SQLite
    df = pd.read_sql(f"SELECT * FROM {table}", sqlite_engine)

    # Пишем данные в PostgreSQL
    df.to_sql(
        table,
        pg_engine,
        if_exists="replace",  # заменяет таблицу в PostgreSQL
        index=False
    )

print("✅ All tables transferred to PostgreSQL")
