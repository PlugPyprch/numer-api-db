from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://xstrojasrxnuga:eae970536638bb67e18411bcbb9338f87cd6675a78de8ad38556c03e4e511315@ec2-44-194-117-205.compute-1.amazonaws.com:5432/d8rtki70e1pi58'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
