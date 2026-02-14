from datetime import date
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator, model_validator


class Loan(BaseModel):
    loan_id: UUID = Field(default_factory=uuid4)
    isbn: str
    member_id: UUID
    loan_date: date = Field(default_factory=date.today)
    due_date: date
    return_date: date | None = None

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("ISBN must contain only digits.")
        if len(v) != 13:
            raise ValueError("ISBN must be exactly 13 digits.")
        return v

    @model_validator(mode="after")
    def validate_dates(self):
        if self.due_date <= self.loan_date:
            raise ValueError("Due date must not be before loan date.")

        if self.return_date is not None:
            if self.return_date <= self.loan_date:
                raise ValueError("Return date must not be before loan date.")
        return self