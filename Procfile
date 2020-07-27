web: flask db upgrade; flask translate compile; gunicorn mycroblog:app
worker: rq worker -u $REDIS_URL mycroblog-tasks
