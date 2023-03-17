import utils.database_utils.RDS_database as _database
import sqlalchemy as _sql

class ST_Prompts(_database.Base):
    """This class defines the 'Predictions' Table.
        Including three columns:
        id: A UUID from a host ID, sequence number, and the current time.
        created_at: A datetime with timezone: Europe/Amsterdam
        predictions: Prediction, whether the two questions are 'Similar' or 'Not similar'

    Args:
        _database (base): sqlalchemy table
    """

    __tablename__ = "st_prompts"
    id = _sql.Column(_sql.String(255), primary_key=True, index=True)
    prompt = _sql.Column(_sql.String(255), unique=False, index=True)