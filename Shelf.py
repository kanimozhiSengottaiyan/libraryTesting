import functions
import Book


Books = {}
class shelfclass():
    def __init__(self):
        self.total=0
        self.numShelves=0
        self.flag=1
        self.shelfName=[]
        self.shelfid=[]

    def shelfCreation(self):
        Books=functions.getDetails_shelf()
        self.temp=functions.getDteails_book()
        self.numShelves = int(input("Enter the  num of shelves :"))
    #   print(Books.keys())
        print(type(Books))
        for i in range(self.numShelves):
            self.shelfid=input("Enter the shelfid :")
            if self.shelfid not in Books:
                self.shelfName = input("Enter the shelfname : ")
                # Booksself.shelfid
                if self.shelfName in Books.keys():
                    Books[self.shelfid] = {'shelf name': self.shelfName}
                    self.temp[self.shelfid]={}
                else:
                    print("Give someother shelfname")
            else:
                print("Shelf is already present")

        print(Books.keys())
        functions.setDetails_book(self.temp)
        functions.setDetails_shelf(Books)

        print("-"* 100)




'''
object.shelfCreation()
object.bookInserting()
object.addBooks()
object.searchBook()
object.shelfDisplay()
'''
book = Book.books()
shelf=shelfclass()


func=True
while(func):
    value=int(input("enter the value from 1 to 5 '\n' 1- For Cretaing Shelf '\n' 2 - For Inserting Books '\n'  3 - For searching Books '\n' 4- To show the Books in the shelf '\n' 5-To display the number of books  "))
    if value==1:
        shelf.shelfCreation()
    if value== 2:

        book.numShelves = shelf.numShelves
        book.shelfid = shelf.shelfid
        book.bookInserting()

    if value == 3:
        book.shelfid = shelf.shelfid
        #book.flag = shelf.flag
        book.find_BookDetails()
    if value == 4:
       # book.flag = shelf.flag
       book.shelfid = shelf.shelfid
       book.shelfDisplay()
    if value==5:
      #  book.total = shelf.total
        book.shelfid = shelf.shelfid
        book.TotalBooks()


'''import Details as d
Books={}

class Book_shelf:
def Create_shelf(self):
self.shelf_id=input('Enter shelfid :')
Books[self.shelf_id]={}



class Book_insert :
def Insert_book(self):
Books=d.Get_Shelf_Details()
self.temp=input('Enter shelfid to insert book :')

if self.temp in Books.keys():
self.Book_id=input('Enter Book id to insert:')
self.Book_name=input('Enter book name :')
self.Book_price=int(input('Enter book price :'))

Books[self.temp][self.Book_id]={'Bookid':self.Book_id,'Bookname':self.Book_name,'price':self.Book_price}


'''