# Используем официальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Allure Commandline
RUN curl -LsS https://dl.bintray.com/qameta/maven/io/qameta/allure/allure/2.13.9/allure-2.13.9.zip -o allure.zip \
    && unzip allure.zip -d /opt/allure \
    && rm allure.zip

# Устанавливаем зависимости Python
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем исходный код в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем переменные окружения для Allure
ENV ALLURE_HOME=/opt/allure
ENV PATH=$ALLURE_HOME/bin:$PATH

# Команда для запуска тестов
CMD ["pytest", "--alluredir=./allure-results"]