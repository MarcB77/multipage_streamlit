import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from dotenv import load_dotenv
import os

load_dotenv()


# AWS
aws_user, aws_passwd, aws_host, aws_port, aws_db = (
    os.environ["DB_USER"],
    os.environ["DB_PWD"],
    os.environ["DB_HOST"],
    "5432",
    os.environ["DB_NAME"],
)

AWS_POSTGRES_url = f"postgresql://{aws_user}:{aws_passwd}@{aws_host}:{aws_port}/{aws_db}"
AWS_engine_postgres = _sql.create_engine(url=AWS_POSTGRES_url, pool_pre_ping=True)

Session_postgres_AWS = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=AWS_engine_postgres
)

Base = _declarative.declarative_base()