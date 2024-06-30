from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullabel=False)
    author = db.Column(db.String(120))
    publisher =db.Column(db.String(120)) 

    def __repr__(self):
        return f"{self.name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in Books:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)

    return{"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "author": book.author, "publisher": book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.sesion.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=["DELETE"])
def delete_book():
    book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return{"message":"deleted"}