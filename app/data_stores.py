import os
import psycopg2

from redis import StrictRedis
import tables
from app_config import Config


redis_conn = StrictRedis(host=Config.REDIS_HOST, port=int(Config.REDIS_PORT))
pg_conn = psycopg2.connect(database=Config.POSTGRES_DB,
                            user=Config.POSTGRES_USER, 
                            password=Config.POSTGRES_PASS,
                            host=Config.POSTGRES_HOST,
                            port=int(Config.POSTGRES_PORT))

# NOTE make sure tables are properly set up ... PG isn't quite as easy as redis :)
tables.Account.create_if_not_exists()

