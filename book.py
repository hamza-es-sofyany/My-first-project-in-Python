from media import Media

class Book(Media):

    def __init__(self, title, author, isbn, available  = True):
        super().__init__(title, author, isbn)
        self.available  = available 
 
    def toggle_availability(self):

        if self.available :
            self.available  = False
        else:
            self.available  = True

    def __str__(self):
        return f" Title is: {self.title} \n Author is: {self.author}\n isbn is: {self.isbn}\n Availabel is: {self.available}" 
    

# print (f"{x.title}...")
