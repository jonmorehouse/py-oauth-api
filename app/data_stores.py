from redis import Redis
import os

redis_conn = Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")))
pq_conn = "hi"


