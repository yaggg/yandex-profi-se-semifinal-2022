from http import HTTPStatus

from flask import Flask
from flask import request
from flask_restx import Api
from flask_restx import Resource
from flask_restx import fields

from app.entities.utils import serialize
from app.storage.auth import AuthorizationService
from app.storage.data_loader import DataLoader

flask_app = Flask(__name__)
app = Api(app=flask_app)
auth_service = AuthorizationService()
data_loader = DataLoader()

auth = app.namespace('auth', description='Authorization')

psql_db = app.namespace('psql', description='PostgreSQL operation')
mongo_db = None  # TODO: not implemented
file_db = app.namespace('file', description='File operation')

preprocessing = app.namespace('preprocessing', description='Data preprocessing')
algorithms = app.namespace('algorithms', description='Data analysis')
visualization = None  # TODO: not implemented

user = app.model('UserModel', {'login': fields.String(required=True, description='login'),
                               'password': fields.String(required=True, description='password')})

psql_source = app.model('PsqlSource', {'url': fields.String(required=True, description='Database URL'),
                                       'table': fields.String(required=True, description='Table')})

mongo_source = None  # TODO: not implemented

file_input = app.model('FileInput', {'path': fields.String(required=True, description='File path')})


@auth.route('/')
class Auth(Resource):

    @auth.doc('Authorization')
    def post(self):
        try:
            data = request.json
            u = auth_service.authorize(data['login'], data['password'])
            return serialize(u), HTTPStatus.OK
        except Exception as e:
            return f'Incorrect login or password: {e}', HTTPStatus.INTERNAL_SERVER_ERROR


@psql_db.route('/<user_id>/read')
class PostgreSQLSource(Resource):

    @psql_db.doc('Upload data from PostgreSQL database')
    def post(self, user_id):
        try:
            data = request.json
            df = data_loader.postgresql_upload(data['connection_url'], data['table'])
            auth_service.add_user_data(user_id, df)
            return 'Success', HTTPStatus.OK
        except Exception as e:
            return f'Exception: {e}', HTTPStatus.INTERNAL_SERVER_ERROR


@file_db.route('/<user_id>/read')
class FileSource(Resource):

    @file_db.doc('Upload data from file')
    def post(self, user_id):
        try:
            data = request.json
            df = data_loader.file_upload(data['path'])
            auth_service.add_user_data(user_id, df)
            return 'Success', HTTPStatus.OK
        except Exception as e:
            return f'Exception: {e}', HTTPStatus.INTERNAL_SERVER_ERROR
