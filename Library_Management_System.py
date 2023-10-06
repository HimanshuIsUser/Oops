import datetime

class Book:
    def __init__(self,ISBN,title,author) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.available_status = False

class Borrowers:
    id = 1
    def __init__(self,name,number,email,age) -> None:
        self.id = Borrowers.id
        self.name = name
        self.number = number
        self.email = email
        self.age = age
        Borrowers.id += 1

    #showing Borrowers Detials
    def borrowers_details(self):
        if isinstance(self,Borrowers):
            data = f'Borrower ID : {self.id}, Name : {self.name}, Number : {self.number}, Email : {self.email}, Age : {self.age}'
        return data

class Transaction:
    _list_of_transaction = []
    status = ["checkin","checkout"]

    # creating transactions  
    def __init__(self,book_object,borrower,return_date,status="checkin") -> None:
            
            if isinstance(book_object,Book):
                self.book = book_object
            else:
                 raise ValueError("first parameter takes only Book object")
            
            if isinstance(borrower,Borrowers):
                self.borrower = borrower
            else:
                 raise ValueError("Second parameter takes only Borrowers object")
            
            self.due_date = datetime.datetime.today().date()

            self.return_date = return_date

            if status in Transaction.status:
                self.status = status

            Transaction._list_of_transaction.append(self)

    # Return all transaction history
    def Transaction_history():
        object = [f'Book Title : {i.book.title}, Borrower Name : {i.borrower.name}, Due_date : {i.due_date}, Return_date : {i.return_date}, Status : {i.status} ' for i in Transaction._list_of_transaction]
        return object
    
    # Return transaction detials of obj
    def specific_history(obj):
        if isinstance(obj,Book):
            data = [f'Book Title : {i.book.title}, Borrower Name : {i.borrower.name}, Due_date : {i.due_date}, Return_date : {i.return_date}, Status : {i.status} ' for i in Transaction._list_of_transaction if i.book.title == obj.title]
        
        elif isinstance(obj,Borrowers):
            data = [f'Book Title : {i.book.title}, Borrower Name : {i.borrower.name}, Due_date : {i.due_date}, Return_date : {i.return_date}, Status : {i.status} ' for i in Transaction._list_of_transaction if i.id == obj.id]
        else:
            data = ["No Data Found"]
        return data
    

class Library:
    _list_of_books = []
    _list_of_borrowers = []

    # Listing Book
    def available_books():
        object = [i.title for i in Library._list_of_books if i.available_status==True]
        return object
    
    # Adding book in library
    def add_book(obj):
        if isinstance(obj,Book):
            library_data = Library._list_of_books
            if not obj in library_data:
                obj.available_status = True
                Library._list_of_books.append(obj)
                return "Book Added successfully"
            return "Book already exists in Library"
        return "You can only parse Book object in this function"
    
    # Removing book from Library
    def remove_book(obj):
        if isinstance(obj,Book):
            library_data = Library._list_of_books
            if obj in library_data:
                obj.available_status = False
                Library._list_of_books.remove(obj)
                return "Book Removed successfully"
            else:
                return "Unable to find this book in Library"
        return "You can only parse Book object in this function" 
    
    # Search Function
    def search_book(title=None,author=None,ISBN=None,available_status=None):
        listdata = []
        if title:
            data = [ i for i in Library._list_of_books if i.title == title]
            listdata += data
        if author:
            data = [ i for i in Library._list_of_books if i.author == author]
            listdata += data
        if ISBN:
            data = [ i for i in Library._list_of_books if i.ISBN == ISBN]
            listdata += data
        if available_status:
            data = [ i for i in Library._list_of_books if i.available_status == available_status]
            listdata += data
        removing_duplicate = set(listdata)
        listdata = list(removing_duplicate)
        converting_objects_into_string = [f'Title : {i.title}, Author : {i.author}, ISBN : {i.ISBN}, Available : {i.available_status}' for i in listdata]
        return converting_objects_into_string
    
    # Adding Borrowers in Library
    def add_borrower(obj):
        if isinstance(obj,Borrowers):
            library_data = Library._list_of_borrowers
            if not obj in library_data:
                Library._list_of_borrowers.append(obj)
                return "New borrower added successfully"
            return "Borrower already exists"
        return "This function accept only Borrower's objects"
    
    # Removing Borrower from Library
    def remove_borrow(obj):
        if isinstance(obj,Borrowers):
            library_data = Library._list_of_borrowers
            if obj in library_data:
                Library._list_of_borrowers.remove(obj)
                return "Borrowers Removed successfully"
            else:
                return "Unable to find this borrowers in Library"
        return "You can only parse Borrowers object in this function" 
    
    # Check-In function
    def check_in(book,borrower,due_date,return_date,status="checkin"):
        if isinstance(book,Book):
            library_data = Library._list_of_books
            borrower_data = Library._list_of_borrowers
            if book in library_data:
                if borrower in borrower_data:
                    obj_data = Transaction(book,borrower,due_date,return_date,status)
                    return "Thank you for choosing our services, come back soon"
                raise ValueError("Borrower is not registered till now")
            raise ValueError("This book is not available right now")
        return "This function accept only Book and Borrower objects"
    
    # Check-Out function
    def check_out(book,borrower,due_date,return_date,status="checkout"):
        obj_data = Transaction(book,borrower,due_date,return_date,status)
        return "Thank you for choosing our services, come back soon"
    






