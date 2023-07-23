from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DbModel(Base):
    __tablename__ = 'pop'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    name = Column(String(20))
    color = Column(String(10))

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return "<Pop('%s', '%s')>" % (self.name, self.color)
