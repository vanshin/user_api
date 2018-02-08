#coding=utf-8

import sys
import os
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UnicodeText, DateTime

Base = declarative_base()

class User(Base):
    '''user'''

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    username = Column(String)
    status = Column(Integer)
    email = Column(String)
    mobile = Column(Integer)
    password = Column(String)
    login_address = Column(String)
    login_time = Column(DateTime)
    regi_time = Column(DateTime)


