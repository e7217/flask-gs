# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, ForeignKey, Integer, SmallInteger, String, Text, UniqueConstraint, Float
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

# mongodb mudules
import mongoengine as me

db = SQLAlchemy()

class Parst(db.Model):
    __tablename__ = 'parst'

    id = Column(Integer, primary_key=True, server_default=db.FetchedValue())
    name = Column(String)
    avg = Column(Float)
    max = Column(Float)
    min = Column(Float)

# mongodb collections 및 documents 정의
class col10(me.Document):
    workno = me.StringField(max_length=200, required=True)
    rackno = me.StringField(max_length=200, required=True)
    type = me.StringField(max_length=200, required=True)
    parameters = me.DictField(max_length=200, required=True)
    created = me.DateTimeField()
    temp = me.FloatField()