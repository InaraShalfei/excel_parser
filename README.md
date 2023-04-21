# excel_parser
Запуск Celery Tasks:
RabbitMQ:docker run -d -p 5672:5672 bitnami/rabbitmq:latest
Celery worker: export DJANGO_SETTINGS_MODULE="excel.settings"; celery -A excel worker --loglevel=INFO
Celery beat: export DJANGO_SETTINGS_MODULE="excel.settings"; celery -A excel beat --loglevel=INFO