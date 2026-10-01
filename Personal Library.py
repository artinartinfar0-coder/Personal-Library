#Personal Library
class Book:
    def __init__(self,title,subject):
        self.title = title
        self.subject = subject
    def chap(self):
        print(self.title, self.subject)
def print_books():
    for i,book in enumerate(books,1):
        print (i, end=". ")
        book.chap()
books = []
while 1:
    i = input('choose one: 1.add 2.remove 3.edit 4.list\n')
    if i == '1':
        title = input('title:')
        subject = input('subject:')
        book = Book(title,subject)
        books.append(book)
    elif i == '2':
        print_books()
        num = int(input('number:'))
        books.pop(num-1)
    elif i == '3':
        print_books()
        num = int (input ('number:'))
        title = input('new title:')
        subject = input('new subject:')
        book = books[num-1]
        book.title = title
        book.subject = subject
    elif i == '4':
        print_books()
    else:
        break