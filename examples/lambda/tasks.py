from celery import task

# @task
# def add(x, y):
#     return x + y

@task
def say():
    print 'say'

if __name__ == '__main__':
    say.s(queue='demien')()
