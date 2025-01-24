import sys
import os

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.models.database import Database

# Тестовая проверка
db = Database()
db.add_note("Тестовая заметка", "2025-01-31", "Пример описания")
print(db.get_notes())