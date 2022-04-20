import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("J.K Rowling")
author_repository.save(author1)
author2 = Author("Steven King")
author_repository.save(author2)

# print(author_repository.select_all())

# print(author_repository.select(1))

# print(author_repository.delete_all())

# author_repository.delete(11)
