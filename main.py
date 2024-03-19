from flask import Flask
from flask_restful import Api, Resource
from resources.res import *
from db.database_generator import *

app = Flask('Mango')
api = Api(app, prefix='/api')

api.add_resource(Greet, '/hello')
api.add_resource(CheckIn, '/checkin')
api.add_resource(CheckOut, '/checkout')
api.add_resource(Logs, '/logs')


# @app.get('/hello')
# def greet():
#     return 'hi'
#
# @app.post('/hello')
# def greet1():
#     return 'hi'
@app.after_request
def after(response):
    print(f'response -> {response.status_code}')
    return response


if __name__ == '__main__':
    init_db()
    app.run(use_reloader=True, debug=True, host='0.0.0.0', port=80)
