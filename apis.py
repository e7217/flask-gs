#-*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource, Api, reqparse
from utils import mongoAgent

class Firstapi(Resource):
    def get(self):
        return {'Hello':'world!!!'}

class WorkComplete(Resource):

    def __init__(self):
        # 작업 완료시
        pass

    def post(self):
        # parsing parameters
        parser = reqparse.RequestParser()
        parser.add_argument('wo_no', type=str)
        parser.add_argument('rack_no', type=str)
        args = parser.parse_args()

        # exec precedure : MES610
        agent = mongoAgent.agent(wo_no=args['wo_no'], rack_no=args['rack_no'])
        agent.conMssql()
        agent.upload_tosql_MES610()
        return {"message":"upload_tosql_MES610"}

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str)
        args = parser.parse_args()
        print("PUT request/response \nmessage:{}".format(args['message']))
        return {"response":"hello world! - put request",
                "message":args['message']}

class CycleComplete(Resource):

    def __init__(self):
        # 한 사이클 완료 시
        pass

    def post(self):
        # parsing parameters
        parser = reqparse.RequestParser()
        parser.add_argument('wo_no', type=str)
        parser.add_argument('rack_no', type=str)
        parser.add_argument('chk_cd', type=str)
        args = parser.parse_args()

        # exec precedure : MES600
        agent = mongoAgent.agent(wo_no=args['wo_no'], rack_no=args['rack_no'], chk_cd=args['chk_cd'])
        agent.conMssql()
        agent.upload_tosql_MES600()
        return {"message":"upload_to_MES600"}