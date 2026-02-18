from media import Media

class Book(Media):
    def __init__(self, title, author, isbn, available=True, type="Book"):
        super().__init__(title, author, isbn)
        self.type = type
        self.available = available
        self.due_date = None
        
    def toggle_availability(self):
        if self.available:
            self.available = False
        else:
            self.available = True

    def __str__(self):
        status = "Available" if self.available else f"Due: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'Borrowed'}"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nType: {self.type}\n{status}"





# from media import Media

# class Book(Media):

#     def __init__(self, title, author, isbn, available  = True):
#         super().__init__(title, author, isbn)
#         self.available  = available 
 
#     def toggle_availability(self):

#         if self.available :
#             self.available  = False
#         else:
#             self.available  = True

#     def __str__(self):
#         return f" Title is: {self.title} \n Author is: {self.author}\n isbn is: {self.isbn}\n Availabel is: {self.available}" 
    

# # print (f"{x.title}...")
