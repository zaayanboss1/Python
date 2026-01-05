class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in sel.bookList:
            print(book)

    def lenBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated.You can taake the book now")
        else:
            print(f"Book is already being used by{self.lendDict[book]}")

    def addbook(self,book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__=='__main__':
    books=Library(['Python','Rich Dad Poor Dad','Harry Potter','C++ Basics','Algorithms by CLRS'],"Let's Upskill")

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue")
        print("1.Display Books")
        print("2. Lend a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")

        els