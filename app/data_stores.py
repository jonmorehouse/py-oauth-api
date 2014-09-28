from redis import Redis
import os

redis = Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")))


