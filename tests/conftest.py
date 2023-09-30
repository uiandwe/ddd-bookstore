import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import registry
from model.conn import Base

from model.book import Book
from domain.book import BookDomain
from services.book_service import BookService


# 매퍼 레지스트리 생성
mapper_registry = registry()

# book 테이블 매핑
mapper_registry.map_imperatively(
    BookDomain,
    Book.__table__
)

# 이 부분은 실제 데이터베이스와 연결되지 않고, 테스트용 메모리 데이터베이스를 사용합니다.
TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture
def db_session():
    # 테스트용 메모리 데이터베이스 생성 및 세션 설정
    engine = create_engine(TEST_DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)  # 테이블 생성

    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture
def book_service(db_session):
    return BookService(db_session)
