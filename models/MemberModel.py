import re
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator, model_validator

from enums.enums import MembershipType


class Member(BaseModel):
    member_id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    age: int
    membership_type: MembershipType
    max_books: int | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("Member name must be at least 2 characters long.")
        return v

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, v):
            raise ValueError("Invalid email format.")

        return v

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int) -> int:
        if not (5 <= v <= 120):
            raise ValueError("Age must be between 5 and 120 years.")
        return v

    @model_validator(mode="after")
    def set_max_books(self):
        if self.membership_type == MembershipType.student:
            self.max_books = 5
        elif self.membership_type == MembershipType.faculty:
            self.max_books = 10
        elif self.membership_type == MembershipType.public:
            self.max_books = 3
        return self