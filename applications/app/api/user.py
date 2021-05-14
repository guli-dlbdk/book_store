from flask import Blueprint, request, session
from flask_restful import Api, Resource
from app.modules.user import (get_user, get_users, create_user,
                               update_user, delete_user,
                               authentication)
from app.api.schema import USER_SCHEMA, LOGIN_SCHEMA
from schema import SchemaError
# from app.api.helpers import login_required

api_bp = Blueprint('user_api', __name__)

api = Api(api_bp)


class AuthResourceApi(Resource):

    def post(self):
        try:
            data = LOGIN_SCHEMA.validate(request.json)
        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}

        result = authentication(data)
        if not result['status']:
            return result
        else:
            user = result['data'][0]
            session['user_id'] = user['id']
            session['user'] = user['name']

        return {'status': 'OK',
                'data': result['data']}

    def delete(self):
        user = session.get('user_id', None)
        if user:
            del session['user_id']
            del session['user']

        return {'status': 'OK'}


class UserResourceApi(Resource):

    def get(self):
        user_id = request.args.get('id', None)
        if user_id:
            admin = get_user(user_id)
            return {'status': 'OK',
                    'data': admin}
        try:
            all_user = get_users()

            return {'status': 'OK',
                    'data': all_user}

        except Exception as e:
            return {'status': 'ERROR',
                    'data': []}


    def post(self):
        try:
            data = USER_SCHEMA.validate(request.json)
        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}

        result, user_id = create_user(**data)
        try:
            return {'status': 'OK' if result else 'ERROR',
                    'id': user_id}

        except Exception as e:
            return {'status': 'ERROR',
                    'id': None}


    # @login_required
    def put(self):
        user_id = request.args.get('id', None)
        if not user_id:
            return {'status': 'ERROR',
                    'message': '\'id\' parametresi girilmeli'}
        try:
            data = USER_SCHEMA.validate(request.json)

        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}

        try:
            result = update_user(user_id, **data)
            return {'status': 'OK' if result else 'ERROR'}

        except Exception as e:
            return {'status': 'ERROR'}


    # @login_required
    def delete(self):
        user_id = request.args.get('id', None)
        if not user_id:
            return {'status': 'ERROR',
                    'message': '\'id\' parametresi girilmeli'}
        result = delete_user(user_id)
        return {'status': 'OK' if result else 'ERROR'}


api.add_resource(UserResourceApi, '/api/user')
api.add_resource(AuthResourceApi, '/api/auth')
