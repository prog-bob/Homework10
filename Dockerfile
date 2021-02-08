# базовый образ
FROM python:3.6

# создать рабочу директорию
WORKDIR /homework10

# установиьть зависимости
COPY requirenments.txt .
#RUN apt-get update -y
#RUN apt-get upgrade -y
#RUN apt-get install python3-pip -y
RUN python3 -m pip install -U pip
RUN python3 -m pip install -r requirenments.txt

# перенести файлы с хоста в контейнер
COPY ./pages ./pages
COPY ./tests ./tests
COPY conftest.py .
COPY pyproject.toml .

EXPOSE 80
EXPOSE 8080
EXPOSE 443

# указать pytest директорию c логами работы тестов для allure
ENTRYPOINT ["pytest",  "--alluredir", "allure-report"]

# изменяемые параметры командной строки
CMD ["--browser", "firefox"]



