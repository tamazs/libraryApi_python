from fastapi import FastAPI

from models.BookModel import Book
from models.LoanModel import Loan
from models.MemberModel import Member

app = FastAPI()

@app.post("/books", response_model=Book)
def add_book(book: Book):
    return book

@app.get("/books/{isbn}", response_model=Book)
def get_book(isbn: str):
    # dummy book since no db
    return Book(
        isbn=isbn,
        title="Example Book",
        author="Author Name",
        publication_year=2020,
        available_copies=5,
        total_copies=5
    )

@app.post("/members", response_model=Member)
def add_member(member: Member):
    return member

@app.post("loans", response_model=Loan)
def add_loan(loan: Loan):
    return loan

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)