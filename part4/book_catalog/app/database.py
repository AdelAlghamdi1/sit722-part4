from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://deakinlab8_2_user:GPSSjl4x1smhSNzdiEXIU7i0mwfJDf10@dpg-crinp4lumphs73cndcng-a.oregon-postgres.render.com/deakinlab8_2")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
