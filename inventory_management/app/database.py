from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://joe_cin_ng_sit722_part_3_user:TAPkBNn1ZI98jal2ClaLXhFoWHyfYDXQ@dpg-cra78723esus739rtlng-a.oregon-postgres.render.com/joe_cin_ng_sit722_part_3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
