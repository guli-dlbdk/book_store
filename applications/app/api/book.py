from flask import Blueprint, request, session
from flask_restful import Api, Resource
from app.modules.book import (find_books, get_books, create_book,
                               update_book, delete_book)
from app.modules.user import (get_user)
from app.api.schema import BOOK_SCHEMA
from schema import SchemaError
from app.api.helpers import login_required

api_bp = Blueprint('book_api', __name__)

api = Api(api_bp)



class BookResourceApi(Resource):
    #@login_required
    def get(self):
        text = request.args.get('text', None)
        try:
            all_book = []
            if not text:
                all_book = get_books()
            else:
                all_book = find_books(text)
            return {'status': 'OK',
                    'data': all_book}
        except Exception as e:
            return {'status': 'ERROR',
                    'data': []}
    #@login_required
    def post(self):
        # todo: tum apilere yapilmalidir.
        # arayuzdeki role yukseltmesini onlemek icin arkaplanda her zaman kontrol etmek lazim.
        # user_id = session.get('user_id', None)
        # user = get_user(user_id)
        # if user[0]['role'] != 'admin':
        #     return {'status': 'ERROR',
        #              'message': 'Yetkiniz yoktur'}
        try:
            data = BOOK_SCHEMA.validate(request.json)
            print('data', data)
        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}
        result = create_book(**data)
        try:
            return {'status': 'OK' if result else 'ERROR'}

        except Exception as e:
            return {'status': 'ERROR'}


    # @login_required
    def put(self):
        # arayuzdeki role yukseltmesini onlemek icin arkaplanda her zaman kontrol etmek lazim.
        # user_id = session.get('user_id', None)
        # user = get_user(user_id)
        # if user[0]['role'] == 'customer':
        #     return {'status': 'ERROR',
        #              'message': 'Yetkiniz yoktur'}

        book_id = request.args.get('id', None)
        if not book_id:
            return {'status': 'ERROR',
                    'message': '\'id\' boş olamaz.'}
        try:
            data = BOOK_SCHEMA.validate(request.json)

        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}

        try:
            result = update_book(book_id, **data)
            return {'status': 'OK' if result else 'ERROR'}

        except Exception as e:
            return {'status': 'ERROR'}


    #@login_required
    def delete(self):
        # arayuzdeki role yukseltmesini onlemek icin arkaplanda her zaman kontrol etmek lazim.
        # user_id = session.get('user_id', None)
        # user = get_user(user_id)
        # if user[0]['role'] != 'admin':
        #     return {'status': 'ERROR',
        #              'message': 'Yetkiniz yoktur'}

        book_id = request.args.get('id', None)
        if not book_id:
            return {'status': 'ERROR',
                    'message': '\'id\' parametresi girilmeli'}
        result = delete_book(book_id)
        return {'status': 'OK' if result else 'ERROR'}


api.add_resource(BookResourceApi, '/api/book')

