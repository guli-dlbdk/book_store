# -----------------------------------------------------------------------------
# BOOK-MODELS.PY
#    
# -----------------------------------------------------------------------------
from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, Boolean,
                        DateTime, text, ForeignKey)
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base




engine = create_engine(DB_URI, echo=False)
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
                'password': self.password,
                'active': self.active,
                'role': self.role}


class Book(Table):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'author': self.author,
                'description': self.description}





Table.metadata.create_all(engine)
