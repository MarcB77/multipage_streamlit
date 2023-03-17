import sqlalchemy.orm as _orm
import utils.database_utils.RDS_database as _database
import utils.database_utils.models as _models


def create_AWS_database():
    return _database.Base.metadata.create_all(bind=_database.AWS_engine_postgres)

def get_db_AWS():
    db_postgres_AWS = _database.Session_postgres_AWS()
    try:
        yield db_postgres_AWS
    finally:
        db_postgres_AWS.close()

def create_prediction(
    db: _orm.Session, UUID: str, prompt: str
):

    db_prompt_data = _models.ST_Prompts(
        id=UUID, prompt=prompt
    )
    db.add(db_prompt_data)
    db.commit()
    db.refresh(db_prompt_data)