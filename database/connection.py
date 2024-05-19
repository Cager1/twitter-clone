from database.base import Base, engine, session
from database.models import user
from database.models import follower
from database.models import tweet

db = session


def migrate():
    print("Creating database tables")
    Base.metadata.create_all(bind=engine)
