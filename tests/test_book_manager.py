from model.book import Book
from domain.book import BookDomain


def test_add_book(book_service):
    # 새 책 도메인 생성
    book_domain = BookDomain(title="Test Book", author="Test Author", year=2022)

    # add_book 메서드 호출
    book_service.add_book(book_domain)

    # 데이터베이스에서 추가된 책 조회
    added_books = book_service.get_books()

    # 책이 추가되었는지 확인
    assert len(added_books) == 1
    added_book = added_books[0]

    # 추가된 책의 정보 확인
    assert added_book.title == "Test Book"
    assert added_book.author == "Test Author"
    assert added_book.year == 2022


def test_get_books(book_service):
    # 데이터베이스에 미리 몇 권의 책 추가
    book1 = Book(title="Book 1", author="Author 1", year=2020)
    book2 = Book(title="Book 2", author="Author 2", year=2021)
    book_service.session.add(book1)
    book_service.session.add(book2)
    book_service.session.commit()

    # get_books 메서드 호출
    books = book_service.get_books()

    # 반환된 책 목록 검증
    assert len(books) == 2
    assert books[0].title == "Book 1"
    assert books[1].title == "Book 2"
