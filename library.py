from datetime import datetime, timedelta
from ebook import Ebook
import csv
from book import Book

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

        if isinstance(select_item, EBook):
            select_user.borrowed_books.append(select_item)
            print("EBook borrowed successfully!")
            return

        if not select_item.available:
            print("Item not available!")
            return

        due_date = datetime.now() + timedelta(days=14)
        select_item.due_date = due_date
        select_item.available = False
        select_user.borrowed_books.append(select_item)
        print(f"Item borrowed successfully! Due: {due_date.strftime('%Y-%m-%d')}")

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
        
        if select_isbn.due_date:
            late_days = (datetime.now() - select_isbn.due_date).days
            if late_days > 0:
                fine = late_days * 1.0
                select_user.balance += fine
                print(f"Fine: ${fine:.1f} ({late_days} days late)")
            select_isbn.due_date = None
        
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

    def load_data(self):
        try:
            with open('books.csv', 'r', encoding='utf-8') as f:                    
                reader = csv.DictReader(f)
                for row in reader:
                    if row['type'] == 'EBook':
                        book = EBook(row['ISBN'], row['title'], row['author'])
                    else:
                        book = Book(row['ISBN'], row['title'], row['author'], row['type'])
                    self.all_books.append(book)
        except FileNotFoundError:
            print("ملف books.csv غير موجود")

    def save_data(self):
        try:
            with open('books.csv', 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['ISBN', 'title', 'author', 'type']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for book in self.all_books:
                    if isinstance(book, EBook):
                        writer.writerow({
                            'ISBN': book.isbn,
                            'title': book.title,
                            'author': book.author,
                            'type': 'EBook'
                        })
                    else:
                        writer.writerow({
                            'ISBN': book.isbn,
                            'title': book.title,
                            'author': book.author,
                            'type': book.type
                        })
        except Exception:
            print("Eror in save:")
