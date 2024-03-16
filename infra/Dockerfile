FROM python:3.12-slim

RUN apt-get update
RUN apt-get -y install gcc

# Основной путь приложения
ENV SRC_DIR=/opt
ENV TESTS_DIR=$SRC_DIR/tests
ENV LOGS_DIR=$SRC_DIR/logs

# Путь до приложения fastapi
ENV APP_DIR=$SRC_DIR/app

ENV APP_USER=order-user

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GUNICORN_PROCESSES=4 \
    GUNICORN_CONNECTIONS=8 \
    GUNICORN_LOGLEVEL='error'

# Создание no-root пользователя
RUN groupadd -r $APP_USER && \
    useradd -d $SRC_DIR -r -g $APP_USER $APP_USER && \
    chown $APP_USER:$APP_USER -R $SRC_DIR && \
    mkdir $LOGS_DIR && \
    chown $APP_USER:$APP_USER -R $SRC_DIR

USER $APP_USER

# Установка зависимостей
WORKDIR $APP_DIR

ENV PATH="/$SRC_DIR/.local/bin:${PATH}"
RUN pip install --user --upgrade pip && \
    pip install --user --no-cache-dir poetry

COPY ./pyproject.toml pyproject.toml
RUN poetry install --no-root --with test

# Копирования кода приложения
COPY ./ $APP_DIR


EXPOSE 8000

COPY infra/entrypoint.sh /usr/local/bin/entrypoint.sh