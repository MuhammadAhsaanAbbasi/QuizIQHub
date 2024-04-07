from starlette.config import Config

# Initialize Config object with path to .env file
try:
    config = Config(".env")
except FileNotFoundError as e:
    print(e)

# Get database URLs from the config object
db_url = config.get("DB_URL")
test_db_url = config.get("TEST_DB_URL")
