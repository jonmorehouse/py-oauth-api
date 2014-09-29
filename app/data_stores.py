from redis import StrictRedis
import os

redis_conn = StrictRedis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")))
