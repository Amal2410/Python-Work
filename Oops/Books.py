class Book:

    title:str

    author:str

    price:int

    language:str

    def __init__(self,title,author,price,language):

        self.title=title

        self.author=author

        self.price=price

        self.language=language

    def display_book(self):

        print(self.title,self.author,self.price)

    def __str__(self):

        return self.title      

book_instance1=Book("rainrising","nirupama",470,"hindi")

book_instance1=Book("goatlife","benyamin",480,"malayalam")

book_instance1.display_book()

print(book_instance1)
