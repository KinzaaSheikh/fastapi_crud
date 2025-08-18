from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# @app.get("/hello/{name}")
# def say_hello(name: str, age: int = 10):
#     return {"message": f"Hello {name}, you are {age} years old"}

class User(BaseModel):
    name: str
    age: int
    email: str
    bio: Optional[str] = "No bio provided!"

@app.post("/user/")
def create_user(user: User):
    return {"message": f"User {user.name} with email {user.email} has been created successfully"}

@app.get("/books/{book_id}")
def get_books(book_id: int, book_title: str):
    return {"book_id": book_id, "book_title": book_title}

class Book(BaseModel):
    title: str
    author: str
    page: int = Field(..., gt=100)

# TODO: add a validation for pages to be at greater than 100

@app.post("/books/")
def create_book(book: Book):
    return {"message": f"Book {book.title} has been created)"}

