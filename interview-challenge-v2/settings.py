import os
from dotenv import load_dotenv


load_dotenv()

UPLOAD_DIR = 'your_path/upload_csv/'


def get_env(variable_name, default=None):
    value = os.getenv(variable_name, default)
    if value and str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"
    return value


# Postgres
# DB_HOST = get_env("DB_HOST", "localhost")
# DB_NAME = get_env("DB_NAME", "postgres")
# DB_USER = get_env("DB_USER", "postgres")
# DB_PASSWORD = get_env("DB_PWD", "password")
#
# DB_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# MySql
os.environ['DB_NAME'] = 'AdviNowDB'
DB_HOST = get_env("DB_HOST", "your_host")
DB_NAME = get_env("DB_NAME", "your_db")
DB_USER = get_env("DB_USER", "your_username")
DB_PASSWORD = get_env("DB_PWD", "your_password")

DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
