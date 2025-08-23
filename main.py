from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    page: int = Field(..., gt=100)
    review: Optional[str] = None

books: List[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to my bookstore!"}

@app.get("/books/")
def get_all_books():
    return books

@app.get("/books/{book_id}")
def get_books(book_id: int, book_title: str):
    return {"book_id": book_id, "book_title": book_title}

@app.post("/books/")
def create_book(book: Book):
    books.append(book)
    return {"message": f"Book {book.title} has been created"}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        books[index] = updated_book
        return {"message": f"Book {book_id} has been updated"}
    return {"error": f"Book {book_id} not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    books.pop(book_id)
    return {"message": f"Book {book_id} has been deleted"}