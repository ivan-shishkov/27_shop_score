import os

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine(os.environ.get('DATABASE_URI'))

Base.prepare(engine, reflect=True)

Order = Base.classes.orders

db_session = scoped_session(sessionmaker(bind=engine))
