from model.book import Book
from domain.book import BookDomain
from sqlalchemy.orm import sessionmaker


class BookService:
    def __init__(self, session):
        self.session = session

    def add_book(self, book_domain: BookDomain):
        session = self.session

        book_domain.validate()  # 비즈니스 로직 검증
        book_model = Book(title=book_domain.title, author=book_domain.author, year=book_domain.year)
        session.add(book_model)
        session.commit()
        session.close()

    def get_books(self):
        session = self.session

        books = session.query(Book).all()
        session.close()
        return [self._map_model_to_domain(book) for book in books]

    def _map_model_to_domain(self, book_model):
        return BookDomain(title=book_model.title, author=book_model.author, year=book_model.year)