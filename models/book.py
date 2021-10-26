from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from models.db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    author = db.Column(db.String(255))
    published_year = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, description, author, published_year):
        self.title = title
        self.description = description
        self.author = author
        self.published_year = published_year
    
    def __repr__(self):
        return f'{self.id} {self.title} {self.author}'
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def json(self):
        return {
            'id': f'{self.id}',
            'title': self.title, 
            'author': self.author, 
            'description': self.description, 
            'published_year': self.published_year,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) if self.updated_at else None
        }
    
    def save(self): 
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
