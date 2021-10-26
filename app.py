import os
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models.db import db
from resources.books import Book, BooksList, NewBook

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
dbname = os.environ.get('DB_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost:5432/{dbname}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.environ.get('SECRET_KEY')

api = Api(app)

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

BASE_URL = '/api/'
api.add_resource(BooksList, f'{BASE_URL}/books')
api.add_resource(NewBook, f'{BASE_URL}/book/new')
api.add_resource(Book, f'{BASE_URL}/book/<string:id>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
