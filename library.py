from ebook import EBook
class Library:
    def __init__(self):
        self.all_books = []
        self.all_users = []
    
    def add_book(self, book):
        for existing_book in self.all_books:
            if existing_book.isbn == book.isbn:
                return

        self.all_books.append(book)
    
    def add_user(self, user):
        self.all_users.append(user)

    def borrow_media(self, user_id, isbn):
        select_user = None
        for user in self.all_users:
            if user.user_id == user_id:
                select_user = user
                break

        select_item = None
        for item in self.all_books:
            if item.isbn == isbn:
                select_item = item
                break

        if select_user is None:
            print("User not found!")
            return
        if select_item is None:
            print("Item not found!")
            return

    # ستب 10: إلا كان EBook نخليه ديما يتسلف
        if isinstance(select_item, EBook):
            select_user.borrowed_books.append(select_item)
            print("EBook borrowed successfully!")
            return

    # Book أو Magazine: منطق عادي
        if not select_item.available:
            print("Item not available!")
            return

        select_item.available = False
        select_user.borrowed_books.append(select_item)
        print("Item borrowed successfully!")

    
    def return_media(self,user_id, isbn):
        select_user = None
        for user in self.all_users:
            if user.user_id == user_id:
                select_user = user
                break

        select_isbn = None
        for book in self.all_books:
            if book.isbn == isbn:
                select_isbn = book
                break

        if select_user is None:
            print("User not found!")
            return
        if select_isbn is None:
            print("Book not found!")
            return
        if select_isbn not in select_user.borrowed_books:
            print("User doesn't have this book!")
            return
        select_isbn.available = True
        select_user.borrowed_books.remove(select_isbn)
        print("Book returned successfully!")
    def search(self,query):
        results = []
        for book in self.all_books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)

        return results
    
    def show_stats(self):
        available_books = 0
        borrowed_books = 0

        for book in self.all_books:
            if hasattr(book, "available"):
                if book.available:
                    available_books += 1
                else:
                    borrowed_books += 1

        print(f"available: {available_books}")
        print(f"Borrowed: {borrowed_books}")
        print(f"Users: {len(self.all_users)}")


        





            
             