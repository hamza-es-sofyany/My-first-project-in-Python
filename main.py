from book import Book
from ebook import Ebook
from user import User
from library import Library

def main_menu():
    lib = Library()
    lib.load_data()
    
    while True:
        print("\n" + "="*40)
        print("🏛️ LIBRARY SYSTEM")
        print("1. 🔍 Search")
        print("2. 📖 Borrow") 
        print("3. 🔙 Return")
        print("4. ➕ Add Book")
        print("5. 💰 Fines")
        print("6. 📊 Stats")
        print("0. 🚪 Exit")
        print("="*40)
        
        choice = input("Choose (0-6): ").strip()
        
        if choice == "0":
            lib.save_data()
            print("✅ Saved & Goodbye!")
            break
            
        elif choice == "1":
            query = input("Search: ")
            results = lib.search(query)
            if results:
                for book in results:
                    print(book)
            else:
                print("No results!")
                
        elif choice == "2":
            try:
                user_id = int(input("User ID: "))
                isbn = input("ISBN: ")
                lib.borrow_media(user_id, isbn)
            except ValueError:
                print("❌ Invalid ID!")
                
        elif choice == "3":
            try:
                user_id = int(input("User ID: "))
                isbn = input("ISBN: ")
                lib.return_media(user_id, isbn)
            except ValueError:
                print("❌ Invalid ID!")
                
        elif choice == "4":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book_type = input("Type (Book/Ebook): ")
            book = Book(title, author, isbn, True, book_type)
            lib.add_book(book)
            print("✅ Added!")
            
        elif choice == "5":
            print("💰 Fines ready (user.balance)!")
            
        elif choice == "6":
            lib.show_stats()
            
        else:
            print("❌ Wrong choice!")

if __name__ == "__main__":
    main_menu()
