import time
import inspect
from celery import Celery

app = Celery('tasks_with_app', broker='redis://localhost:6379/0')
app.conf.CELERY_ACCEPT_CONTENT = ['json']
app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.CELERY_RESULT_SERIALIZER = 'json'

@app.task
def add(self, x, y):
    return x + y

@app.task
def dummy():
    print 'in dummy'
