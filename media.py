class Media:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.due_date = None
        self.type = "Media"
        
    def __str__(self):
        status = "Available" if self.available else f"Due: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'Borrowed'}"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nType: {self.type}\n{status}"
