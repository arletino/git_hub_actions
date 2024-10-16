# --- Базовый этап для установки зависимостей и тестов ---
FROM python:3.12-slim AS test

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src

# Устанавливаем системные зависимости
RUN pip install poetry

# Копируем оставшиеся файлы проекта
COPY pyproject.toml poetry.lock ./

# Отключаем создание виртуальных сред
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости
RUN poetry install --no-interaction --no-ansi

# Копируем проект
COPY app ./app

# Копируем тесты
COPY test ./test

CMD ["poetry", "run", "pytest"]