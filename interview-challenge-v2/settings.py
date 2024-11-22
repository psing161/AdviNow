import os
from dotenv import load_dotenv


load_dotenv()

UPLOAD_DIR = '/Users/pratimasingh/Documents/Internship/interview-challenge-v2/upload_csv/'


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
DB_HOST = get_env("DB_HOST", "127.0.0.1")
DB_NAME = get_env("DB_NAME", "AdviNowDB")
DB_USER = get_env("DB_USER", "root")
DB_PASSWORD = get_env("DB_PWD", "root")

DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
