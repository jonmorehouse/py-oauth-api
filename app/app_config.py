from config import Config

# TODO: set up logger or modify my Config library
Config.load_from_list(["REDIS_HOST",
    "REDIS_PORT",
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "POSTGRES_USER",
    "POSTGRES_PASS",
    "POSTGRES_DB",
    ])
