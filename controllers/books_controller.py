from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

tasks_blueprint = Blueprint("books", __name__)


@tasks_blueprint.route("/books")
def books():
    books = book_repository.select_all()  # NEW
    return render_template("books/book.html", all_books=books)


@tasks_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
