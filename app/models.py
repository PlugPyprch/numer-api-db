from sqlalchemy import  Column, Integer, String
from app.config import Base

class Equa(Base):
    __tablename__ ="equation"

    id = Column(Integer, primary_key=True, index=True)
    function = Column(String)
    equation = Column(String)