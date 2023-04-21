from .celery import app
from apps.excel_parser.views import parse_file


@app.task
def parse_excel():
    parse_file(None)


app.conf.beat_schedule = {
    'daily_parser': {
        'task': 'excel.tasks.parse_excel',
        'schedule': 10.0,
        'args': ()
    },
}
