from media import Media

class Magazine(Media):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number
