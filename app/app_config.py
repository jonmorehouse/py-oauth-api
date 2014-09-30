from config import Config

# NOTE load database credentials from local env
Config.load_from_list([
    "REDIS_HOST",
    "REDIS_PORT",
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "POSTGRES_USER",
    "POSTGRES_PASS",
    "POSTGRES_DB",
    ])

# NOTE load in twilio api information from local env
Config.load_from_list([
    "TWILIO_AUTH_TOKEN",
    "TWILIO_AUTH_SID",
    "TWILIO_PHONE_NUMBER",
    ])

# NOTE application configuration settings
Config.load_from_list([
    "ACTIVATION_TTL"

    ])
