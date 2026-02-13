# from book import Book
# from user import User
# from library import Library

# book1 = Book("habits ", "L3arbi ", "001")
# book2 = Book("habits2", "bojm3a", "002")
# book3 = Book("HABITS3", "hmad", "003")
# book4 = Book("HAbiTs4", "hassan", "004")
# book5 = Book("walo", "hamza", "006")

# user1 = User("Ahmed", 1, [])
# user2 = User("Ali", 2, [])

# library = Library()

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.add_book(book4)
# library.add_book(book5)

# library.add_user(user1)
# library.add_user(user2)

# print(f"Total books: {len(library.all_books)}")
# print(f"Total Users: {len(library.all_users)}")

from book import Book
from user import User
from library import Library

if __name__ == "__main__":
    book1 = Book("habits", "L3arbi", "001")
    book2 = Book("habits2", "bojm3a", "002")
    book3 = Book("HABITS3", "hmad", "003")
    book4 = Book("HAbiTs4", "hassan", "004")
    book5 = Book("walo", "hamza", "006")

    user1 = User("Ahmed", 1, [])
    user2 = User("Ali", 2, [])

    library = Library()

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    library.add_user(user1)
    library.add_user(user2)

    print(f"Total books: {len(library.all_books)}")
    print(f"Total users: {len(library.all_users)}")

    library.show_stats()

    library.borrow_media(1, "001")
    library.show_stats()

    library.borrow_media(1, "001")

    res = library.search("habits")
    for b in res:
        print(f"*** {b} ***")

    library.return_media(1, "001")
    library.show_stats()

    library.return_media(2, "001")
