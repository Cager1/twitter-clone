# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# load environment variables
from dotenv import load_dotenv
load_dotenv()
user = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
table = os.getenv("DATABASE_TABLE")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")

DATABASE_URL = f"mysql://{user}:{password}@{host}:{port}/{table}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()
