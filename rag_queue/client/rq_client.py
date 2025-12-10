from redis import Redis
from rq import Queue

queue = Queue(connection=Redis(
    host='vector-db',
    port=6379
))