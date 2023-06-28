from sqlalchemy import Column, Integer, String, BIGINT
from config import Base

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(BIGINT)
    