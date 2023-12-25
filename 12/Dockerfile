FROM python:3.8
WORKDIR /home/statistic_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /home/statistic_app/requirements.txt
RUN pip install -r requirements.txt

COPY ./statistic_app /home/statistic_app
