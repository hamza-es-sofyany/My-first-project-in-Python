from media import Media

class Magazine(Media):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.type = "Magazine"
        self.issue_number = issue_number
        self.available = True
        self.due_date = None
        
    def __str__(self):
        status = "Available" if self.available else f"Due: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'Borrowed'}"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nType: {self.type}\nIssue: {self.issue_number}\n{status}"
