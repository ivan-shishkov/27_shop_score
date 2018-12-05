import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, DateTime

Base = declarative_base()

engine = create_engine(os.environ.get('DATABASE_URI'))

db_session = scoped_session(sessionmaker(bind=engine))


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, index=True, nullable=False)
    confirmed = Column(DateTime, index=True)
