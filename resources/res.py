import datetime
from db.database_generator import *
from flask_restful import Resource
from flask import request


def request_validation(data, *keys):
    for key in keys:
        if key not in data.keys():
            return key
    return None


class Greet(Resource):
    def get(self):
        return 'hello get'

    def post(self):
        return 'hello post'

    def put(self):
        pass

    def delete(self):
        pass


class CheckOut(Resource):

    def post(self):
        data = request.json
        val = request_validation(data, 'client_id')
        if val:
            return {'status': 'error', 'message': f'missing -- {val} --'}, 400
        client= data['client_id']
        current_time= datetime.datetime.now()
        insert_end_time(client,current_time)
        return {'status': 'success', 'message': 'have a nice day'}

    def put(self):
        pass

    def delete(self):
        pass


class CheckIn(Resource):

    def post(self):
        data = request.json
        val = request_validation(data, 'location','client_id')
        if val:
            return {'status': 'error', 'message': f'missing -- {val} --'},400
        location = data['location']
        client = data['client_id']
        date = datetime.datetime.now()

        insert_start_time(client,date,location)

        response = {'status': 'success', 'message': 'parking is valid'}
        return response

    def put(self):
        pass

    def delete(self):
        pass


class Logs(Resource):
    def get(self):
        data = request.json
        val = request_validation(data, 'client_id')
        if val:
            return {'status': 'error', 'message': f'missing -- {val} --'}, 400
        client = data['client_id']
        res = get_sessions_by_user(client)
        print(res)
        return res

    def post(self):
        return 'hello post'

    def put(self):
        pass

    def delete(self):
        pass
