from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


class Book(BaseModel):
    isbn: str
    title: str
    author: str
    publication_year: int
    available_copies: int
    total_copies: int

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("ISBN must contain only digits.")
        if len(v) != 13:
            raise ValueError("ISBN must be exactly 13 digits.")
        return v

    @field_validator("title", "author")
    @classmethod
    def validate_non_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field cannot be empty.")
        return v

    @field_validator("publication_year")
    @classmethod
    def validate_publication_year(cls, v: int) -> int:
        current_year = datetime.now().year
        if v < 1000 or v > current_year:
            raise ValueError(f"Publication year must be between 1000 and {current_year}.")
        return v

    @field_validator("available_copies")
    @classmethod
    def validate_available_copies(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Available copies cannot be negative.")
        return v

    @field_validator("total_copies")
    @classmethod
    def validate_total_copies(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Total copies must be greater than 0.")
        return v

    @model_validator(mode="after")
    def validate_copies_logic(self):
        if self.available_copies > self.total_copies:
            raise ValueError("Available copies cannot exceed total copies.")
        return self
