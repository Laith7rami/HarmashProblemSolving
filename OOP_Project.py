class Author:
    ID = 0
    authors = []

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        Author.ID += 1
        self.ID = Author.ID
        Author.authors.append(self)
        self.books = []


a = Author("ahmed", 234560, "oidpas")
b = Author("ali", 234560, "oidpas")


class Book:
    ID = -1
    book = []

    def __init__(self, title, publishing_at, version, author):
        Book.ID += 1
        self.ID = Book.ID
        self.title = title
        self.publishing_at = publishing_at
        self.version = version
        self.author = self.search_auth(author)
        Book.book.append(self)

    def search_auth(self, author):
        for i in Author.authors:
            if i.name == author:
                print("auther true")
                i.books.append(self)
                return i
        print("sorry the author not exit")  # \ndo you add author\nyes\tno")

        return "unknown"


new = Book("google", "2018/6/7", 4.6, "ali")
new1 = Book("machine learning", "2018/6/7", 4.6, "ali")
new3 = Book("cs50", "2018/6/7", 4.6, "p0")


class Library:

    @staticmethod
    def Add_Author(name, phone, email):
        Author(name, phone, email)

    @staticmethod
    def remove_author(id):
        for i in Author.authors:
            if i.ID == id:
                Author.authors.remove(i)
                return 0
        print("Sorry the ID is not exist")

    @staticmethod
    def print_info(id):
        for i in Author.authors:
            if i.ID == id:
                print(f"name: {i.name}\nPhone number: {i.phone}\nEmail: {i.email}")
                return 0
        print("Sorry the ID is not exist")

    @staticmethod
    def author_books(id):
        for i in Author.authors:
            # print(f"{i.ID} == {id} {len(Author.authors)}")
            if i.ID == id:
                for j in i.books:
                    print(f"{j.title}")
                return 0

    @staticmethod
    def add_book(title, publishing_at, version, author):
        Book(title, publishing_at, version, author)
    @staticmethod
    def remove_book(id):
        for i in Book.book:
            if id == i.ID:
                Book.book.remove(i)
                return 0
        print("the book not exist")

    @staticmethod
    def print_book(id):
        for i in Book.book:
            if id == i.ID:
                print(f"name:{i.title}\npublishing:{i.publishing_at}\nversion:{i.version}\nauthor:{i.author.name}")
                return 0
        print("the book is not exist")


Library.author_books(b.ID)
#print(Book.book[0].ID)
Library.remove_book(0)
Library.print_book(1)