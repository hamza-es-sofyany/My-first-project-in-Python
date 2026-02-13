from media import Media

class Ebook(Media):

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)