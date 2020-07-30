"""
marshmallow :
복잡한 데이터 타입을 네이티브 파이썬 데이터 타입으로 변환 및 역변환
입력 데이터 유효성 검사, 역직렬화
직렬화
"""
# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, ForeignKey, Integer, SmallInteger, String, Text, UniqueConstraint, Float
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

# marshmallow
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

# mongodb mudules
import mongoengine as me
from flask_mongoengine import MongoEngine

db = SQLAlchemy()
mdb = MongoEngine()
ma = Marshmallow()

class AddUpdateDelete():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class Parst(db.Model):
    __tablename__ = 'parst'

    id = Column(Integer, primary_key=True, server_default=db.FetchedValue())
    name = Column(String)
    avg = Column(Float)
    max = Column(Float)
    min = Column(Float)

# mongodb collections 및 documents 정의
class testtb01(me.Document):
    workno = me.StringField(max_length=200, required=True)
    rackno = me.StringField(max_length=200, required=True)
    type = me.StringField(max_length=200, required=True)
    parameters = me.DictField(max_length=200, required=True)
    created = me.DateTimeField()
    temp = me.FloatField()

class getdata(mdb.Document):
    wo_no = mdb.StringField(max_length=200, required=True)
    rack_no = mdb.StringField(max_length=200, required=True)
    chk_no = mdb.StringField(max_length=200, required=True)
    param = mdb.StringField(max_length=200, required=True)
    value = mdb.StringField(max_length=200, required=True)
    chk_tm = mdb.DateTimeField()

class col10(mdb.DynamicDocument):
    workno = mdb.StringField(max_length=200, required=True)
    rackno = mdb.StringField(max_length=200, required=True)
    type = mdb.StringField(max_length=200, required=True)
    parameters = mdb.DictField(max_length=200, required=True)
    created = mdb.DateTimeField()
    temp = mdb.FloatField()

class bGetdataSchema(ma.Schema):
    wo_no = fields.String()
    rack_no = fields.String()
    chk_no = fields.String()
    param = fields.String()
    value = fields.String()
    chk_tm = fields.DateTime()

class machineinfo(mdb.Document):
    machine = mdb.StringField(max_length=200, required=True)
    param = mdb.StringField(max_length=200, required=True)
    value = mdb.StringField(max_length=200, required=True)
