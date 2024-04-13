from starlette.config import Config

# Initialize Config object with path to .env file
try:
    config = Config(".env")
except FileNotFoundError as e:
    print(e)

# Get database URLs from the config object
db_url = config.get("DB_URL")
test_db_url = config.get("TEST_DB_URL")

access_expiry_time = config.get("ACCESS_EXPIRY_TIME")
refresh_expiry_time = config.get("REFRESH_EXPIRY_TIME")

SECRET_KEY = config("SECRET_KEY", cast=str)
ALGORITHM = config("ALGORITHM", cast=str)
