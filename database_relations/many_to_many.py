from xmlrpc.client import DateTime
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# mysql://root:123456y@127.0.0.1/test
engine = create_engine('sqlite://', echo=True)
Base = declarative_base()

# association_table = Table('bookauthors', Base.metadata,
#     Column('author_id', ForeignKey('authors.id'), primary_key=True),
#     Column('book_isbn', ForeignKey('books.isbn'), primary_key=True)
# )

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Book(Base):
    __tablename__ = 'books'
    isbn = Column(String(11), primary_key=True)
    title = Column(String(50), nullable=False)


class BookAuthor(Base):
    __tablename__ = 'booksauthors'
    author_id = Column(ForeignKey('authors.id'), primary_key=True)
    book_isbn = Column(ForeignKey('books.isbn'), primary_key=True)


authors = [
    Author(name='Svetoslav Georgiev'),
    Author(name='Ivan Ivanov'),
    Author(name='Alex Georgiev'),
    Author(name='Yavor Radev')
]

books = [
    Book(isbn='123-123-123', title='Game of thrones'),
    Book(isbn='123-123-124', title='Shadows'),
    Book(isbn='123-123-000', title='Hrana'),
    Book(isbn='123-123-125', title='Pipi dulgoro chorapche')
]

booksauthors = [
    BookAuthor(author_id=1 , book_isbn='123-123-123'),
    BookAuthor(author_id=2 , book_isbn='123-123-124'),
    BookAuthor(author_id=3 , book_isbn='123-123-125'),
    BookAuthor(author_id=2 , book_isbn='123-123-125')
]


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all(authors)
session.commit()

session.add_all(books)
session.commit()

session.add_all(booksauthors)
session.commit()

for x in session.query(Author, Book).filter(BookAuthor.author_id == Author.id, BookAuthor.book_isbn == Book.isbn).all():
   print (f"Author: {x.Author.name}\nBook: {x.Book.title}\n")

