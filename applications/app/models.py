# -----------------------------------------------------------------------------
# BOOK-MODELS.PY
#    
# -----------------------------------------------------------------------------
from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, Boolean,
                        DateTime, text, ForeignKey)
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from operator import itemgetter
import datetime


engine = create_engine(DB_URI,  echo=False )
Session = sessionmaker(bind=engine)
Table = declarative_base()
Table.metadata.bind = engine



class User(Table):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)
    password = Column(String(255), nullable=False)

    active = Column(Boolean, index=True, nullable=True,
                    server_default=text("true"))

    role = Column(String(30),nullable=False)

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'active': self.active,
                'role': self.role}








Table.metadata.create_all(engine)
