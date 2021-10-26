from flask_restful import Resource, reqparse
from itsdangerous import exc

from models.book import BookModel


class BooksList(Resource):
    def get(self):
        '''
        Retrieve a list of all the books in the database.
        '''
        return {'books': [book.json() for book in BookModel.query.all()]}


class NewBook(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    parser.add_argument(
        'author',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    parser.add_argument(
        'published_year',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    def post(self):
        data = self.parser.parse_args()
        book = BookModel(**data)

        try:
            book.save()
        except:
            return {'message': 'internal server error while trying to save book'}, 500
        
        return book.json()

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    parser.add_argument(
        'author',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    parser.add_argument(
        'published_year',
        type=str,
        required=True,
        help='This field cannot be blank'
    )
    
    def get(self, id):
        try:
            book = BookModel.find_by_id(id)
        except:
            return {'message': 'internal error while trying to get book'}, 505
            
        if not book:
            return {'message': 'Book with the given id not found'}, 404

        return book.json()
    
    def put(self, id):
        pass

    def delete(self, id):
        try:
            book = BookModel.find_by_id(id)
        except:
            return {'message': 'internal error while trying to get book'}, 505
        
        if not book:
            return {'message': 'Book with the given id not found'}, 404
        
        book.delete()
        return {'message': 'Successfully deleted book'}

            
