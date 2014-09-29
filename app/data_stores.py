import os

from redis import StrictRedis
import psycopg2


redis_conn = StrictRedis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")))
pg_conn = psycopg2.connect(database = 
