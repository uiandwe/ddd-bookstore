from __future__ import annotations
from datetime import date
from typing import Optional, Set


# 도메인 클래스 정의
class BookDomain:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def validate(self):
        # 비즈니스 로직: 책의 제목과 작가는 필수 정보입니다.
        if not self.title or not self.author:
            raise ValueError("책의 제목과 작가는 필수 정보입니다.")