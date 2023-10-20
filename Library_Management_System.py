import datetime

class Book:
    def __init__(self,ISBN,title,author) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.available_status = False

class Borrowers:
    _list_of_borrowers_email = []
    id = 1
    def __init__(self,name,number,email,age) -> None:
        self.id = Borrowers.id
        self.name = name
        self.number = number
        self.email = email
        self.age = age
        emailList = [i.email for i in Borrowers._list_of_borrowers_email]
        if email in emailList:
            return ValueError("You are already registered.., Try wiht another Email id")
        Borrowers._list_of_borrowers_email.append(self)
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
    def __init__(self,book_object,due_date,borrower,return_date,status="checkout") -> None:
            
            if isinstance(book_object,Book):
                self.book = book_object
            else:
                 raise ValueError("first parameter takes only Book object")
            
            if isinstance(borrower,Borrowers):
                self.borrower = borrower
            else:
                 raise ValueError("Second parameter takes only Borrowers object")
            
            self.due_date = due_date

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
                return True
            return False
        return "You can only parse Book object in this function"
    
    # Removing book from Library
    def remove_book(obj):
        if isinstance(obj,Book):
            library_data = Library._list_of_books
            if obj in library_data:
                obj.available_status = False
                Library._list_of_books.remove(obj)
                return True
            else:
                return False
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
                return True
            return False
        return False
    
    # Removing Borrower from Library
    def remove_borrow(obj):
        if isinstance(obj,Borrowers):
            library_data = Library._list_of_borrowers
            if obj in library_data:
                Library._list_of_borrowers.remove(obj)
                return True
            else:
                return False
        return "You can only parse Borrowers object in this function" 
    
    # Check-In function
    def check_in(book,borrower,due_date,return_date,status="checkin"):
        if isinstance(book,Book):
            library_data = Library._list_of_books
            borrower_data = Library._list_of_borrowers
            if not book in library_data:
                if borrower in borrower_data:
                    book.available_status = True
                    obj_data = Transaction(book,borrower,due_date,return_date,status)
                    return "Thank you for choosing our services, come back soon"
                raise ValueError("Borrower Not registered")
            raise ValueError("This book is already exists in library!!")
        return "This function accept only Book and Borrower objects"
    
    # Check-Out function
    def check_out(book,borrower,due_date,return_date,status="checkout"):
        if isinstance(book,Book):
            library_data = Library._list_of_books
            borrower_data = Library._list_of_borrowers
            if book in library_data:
                if borrower in borrower_data:
                    book.available_status = False
                    obj_data = Transaction(book,borrower,due_date,return_date,status)
                    return "Thanks for returning the book"
                raise ValueError("Unidentified Borrower!! Please register yourself as a borrower first...")
            raise ValueError("This book is already taken by someone else!!")
        return "This function accept only Book and Borrower objects"
    

if __name__=="__main__":
    print("Welcome to the Library!!")
    currentuser = {}

    while True:
        print( " \n\n\tChoose One Of Your Action !!")
        print("\n1 Books Queries","\t\t2 Borrower Queries\n","\n3 Check In !!","\t\t\t4 Check Out !!")
        userinput = int(input("\nEnter your option : "))
        if userinput>4 or userinput<1:
            finalinput = input("\nPlease choose correct option, To Exit press Y : ")
            if finalinput=="Y":
                print("\nSee You soon...")
                break
            else:
                continue
        elif userinput==2:
            print("\n1 Registeration","\t\t2 Remove your account")
            userinput = int(input("\nChoose your next step : "))
            if userinput>2 or userinput<1:
                finalinput = input("\nPlease choose correct option, Back to main meny press X : ")
                if finalinput=="X":
                    continue
            elif userinput == 1:
                name = str(input("Enter your name : "))
                email = str(input("Enter your email id : "))
                age = int(input("Ente your age in Years : "))
                number = str(input("Enter your number : "))
                borrower_object = Borrowers(name,number,email,age)
                currentuser["borrower"] = borrower_object
                # print(borrower_object.id)
                borrower_result = Library.add_borrower(borrower_object)
                if borrower_result == True:
                    print("\nborrower added successfully")
                else:
                    print("\nYou are already registered")
                continue
            else:
                if currentuser.get("borrower"):
                    remove_borrower = Library.remove_borrow(currentuser['borrower'])
                    if remove_borrower == True:
                        print("\nYour account removed from library")
                    elif remove_borrower == False:
                        print("\nFirst your have to registered yourself as a borrower in library")
                    else:
                        print(remove_borrower)
                else:
                    print("\nYou did not registered yet!! Do it first...")
                continue
        elif userinput == 1:
            print("\n\tchoose one of the given option\n","\n1 Add Book","\t\t2 Remove Book","\n\n3 Search Book")
            userinput = int(input("\nEnter Your next step or Enter X for exit : "))
            if userinput == "X":
                print("\nSee you soon....")
                break
            elif userinput == 1:
                title = input("Enter the title for your book : ")
                ISBN = input("Enter the ISBN for your book : ")
                author = input("Enter the author for your book : ")
                book_object = Book(ISBN,title,author)
                book_result = Library.add_book(book_object)
                if book_result == True:
                    print("\nYour book added successfully")
                    if currentuser.get("book"):
                        currentuser['book'].append(book_object)
                    else:
                        currentuser['book'] = [book_object]
                    continue
            elif userinput == 2:
                if currentuser.get("book"):
                    book_list = [i.title for i in currentuser['book']]
                    print("\n"," ".join(book_list))
                    remove_book = input("\nEnter the title of the book, which you want to remove from library : ")
                    if remove_book in book_list:
                        index_values = book_list.index(remove_book)
                        book_object = currentuser['book'][index_values]
                        result_removal_book = Library.remove_book(book_object)
                        if result_removal_book == True:
                            print(f'\nThe {remove_book} book is removed successfully...')
                            currentuser['book'].remove(book_object)
                        elif result_removal_book == False:
                            print("\nThis is not available to removed")
                        else:
                            print(f'\n {result_removal_book}')
                    else:
                        print("\nNot Found, Try again...")
                    continue
                else:
                    print("\nYou can only remove your added books.. So first try to add your book first !!")
            elif userinput == 3:
                book_title = input("\nIf you are looking for any book, you can simplily enter its title here : ")
                book_data = Library._list_of_books
                for i in book_data:
                    if i.title == book_title:
                        print(f'\n{i.title}, {i.ISBN}, {i.author}, {i.available_status}')
                        print("\n Check the available status for this book, if you want to check in !!")
                        continue
                    else:
                        pass
            else:
                continue
        elif userinput == 3:
            book_data = Library._list_of_books
            list_data = [f'{i.title}' for i in book_data if i.available_status == True]
            print(" ".join(list_data))
            userinput = input('\n Please Enter the Title of the book, which you want to Check In ! : ')
            if userinput in list_data:
                index_number = list_data.index(userinput)
                book_object = book_data[index_number]
                if currentuser["borrower"]:
                    borrower = currentuser["borrower"]
                    due_date = datetime.datetime.today()
                    user_date_for_return = input("Enter the date formatted as YYYY-MM-DD to return this book : ").split('-')
                    year,month,day = [int(i) for i in user_date_for_return]
                    return_date = datetime.date(year,month,day)
                    check_in_object = Library.check_out(book_object,borrower,due_date,return_date)
                    continue
                else:
                    print("\nYou need to registered yourself as a borrower.....")
                    continue
            else:
                print("\nYou haven't choosen a valid book!, Try again.......")
                continue
        elif userinput == 4:
            user_input = input("\nEnter the title of your book, which you want to return : ")
            book_data = Library._list_of_books
            list_data = [f'{i.title}' for i in book_data if i.available_status == False]
            if user_input in list_data:
                index_number = list_data.index(userinput)
                book_object = book_data[index_number]
                if currentuser["borrower"]:
                    borrower = currentuser["borrower"]
                    transactionList = Transaction._list_of_transaction
                    object = [i for i in transactionList if i.book.available_status ==False and i.status == "checkout" and i.borrower == borrower]
                    due_date = object.due_date
                    return_date = datetime.datetime.today()
                    check_in_object = Library.check_in(book_object,borrower,due_date,return_date)
                    book_object.available_status = True
                    object.status = "Checkin"
                    continue
                else:
                    print("\nYou have not registered yourself as a borrower yet...")
                    continue
            else:
                print("\nNot a valid book....")
                continue
        else:
            print("\nYou have choosen a wrong option!, Try again....")
            continue






                    
    

        continue
