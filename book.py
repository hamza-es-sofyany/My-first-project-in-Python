class Book:

    def __init__(self, title, author, isbn, Available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.Available = Available

    def toggle_availability(self):

        if self.Available:
            self.Available = False
        else:
            self.Available = True

    def __str__(self):
        return f" Title is: {self.title} \n Author is: {self.author}\n isbn is: {self.isbn}\n Availabel is: {self.Available}" 
    

# print (f"{x.title}...")
