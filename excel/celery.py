import os

from celery import Celery

user = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')
app = Celery('excel', broker=f'amqp://user:bitnami@localhost', include=['excel.tasks'])

if __name__ == '__main__':
    app.start()
