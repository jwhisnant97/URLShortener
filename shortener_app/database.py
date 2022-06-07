# shortener_app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']
if DATABASE_URL and DATABASE_URL.startswith("postgres/"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

conn = psycopg2.connect(DATABASE_URL,sslmode='require')

engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(
    autocommit = False, autoflush=False, bind=engine
)
Base = declarative_base()

