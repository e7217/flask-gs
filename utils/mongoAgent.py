#-*- coding: utf-8 -*-

import os, sys
# 부모폴더의 절대 경로를 참조 path에 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import numpy as np
import pandas as pd

# MongoDB 접속 모듈
import mongoengine as me

# mssql 접속 모듈
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, NCHAR, SmallInteger, Table, Unicode, create_engine
from sqlalchemy.dialects.mssql import BIT, DATETIME2
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import time, datetime, config
from models import getdata

class agent(object):

    def __init__(self,
                 wo_no='',
                 rack_no='',
                 chk_cd='',
                 chk_nm='',
                 param='',
                 value='',
                 chk_tm=datetime.datetime.now()):
        """
        :param wo_no:       작업지시번호
        :param rack_no:     상대적 랙 번호
        :param chk_cd:      작업조건 코드
        :param chk_nm:      작업조건명
        :param param:       측정항목명
        :param value:       측정값
        :param chk_tm:      데이터 측정 시간
        """
        self.wo_no = wo_no
        self.rack_no = rack_no
        self.chk_cd = chk_cd
        self.chk_nm = chk_nm
        self.param = param
        self.value = value
        self.chk_tm = chk_tm

    def conMssql(self):
        mssqlEngine = create_engine('mssql+pymssql://SA:Root1234!@@e7217.synology.me:1566/sf', echo=True)
        Session = sessionmaker(bind=mssqlEngine)
        session = Session()
        session.commit()
        pass

    def upload_tosql_MES610(self):
        pass

    def upload_tosql_MES600(self):
        pass

    def setMongoConfig(self, dictionary):
        self.mongoEngine = me.connect(db =dictionary['database'],
                                      username=dictionary['username'],
                                      password=dictionary['password'],
                                      host=dictionary['host'])

    def disconnectMongo(self):
        me.disconnect()

    def parser(self):
        """
        key를 매개체로 해서 value들의 합, 최소값, 최소값, 평균값 dict집합을 리턴한다.
        :return: ex) {'_id': '운전/정지', 'sum': 259961, 'min': 0, 'max': 513, 'avg': 1.0117379205666583}
        """
        ## aggregation
        pipeline = [
            {
                "$group":
                    {
                        "_id":"$key",
                        "sum":{
                            "$sum":"$value"
                        },
                        "min":{
                            "$min":"$value"
                        },
                        "max":{
                            "$max":"$value"
                        },
                        "avg":{
                            "$avg":"$value"
                        }

                    }
            }
        ]
        return getdata.objects().aggregate(pipeline)

agent = agent()
agent.setMongoConfig(config.mongoConfig)
start = time.time()
result = agent.parser()
end = time.time()
for i in result:
    print(i)
print(end-start)
print('connection : ', agent.mongoEngine)
agent.disconnectMongo()
print('connection : ', agent.mongoEngine)