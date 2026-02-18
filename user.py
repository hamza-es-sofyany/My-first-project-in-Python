class User:
    def __init__(self, name, user_id, borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books
        self.balance = 0.0

    def display_user_info(self):
        print(f"User: {self.name}")
        if not self.borrowed_books:
            print("No books borrowed")
        else:
            titles = []
            for book in self.borrowed_books:
                titles.append(book.title)
            print(f"Borrowed books: {', '.join(titles)}")
            print(f"Balance: ${self.balance}")
