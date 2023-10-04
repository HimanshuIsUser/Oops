# class Book():
#     def __init__(self,isbn,title,author,publisher,pages,copies,price):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.copies = copies
#         self._price = price

#     def display(self):
#         print(self.isbn,self.title,self.price,self.copies)
#         return ''
    
#     def In_stock(self):
#         if self.copies > 0:
#             return True
#         return False
#     def sell(self):
#         if self.In_stock():
#             self.copies -= 1
#             return 
#         return "The book is out of stock"
    
#     @property
#     def price(self):
#         return self._price
    
#     @price.setter
#     def price_set(self,price):
#         if 50<price<1000:
#             self._price=price 
#             return print(self.display())
#         else:
#             raise ValueError("Value should be more then 50 and less then 1000")
        


# book1 = Book("1111111111","learn physics","stephen","CBC",350,200,10)
# book2 = Book("2222222222","learn chemistry","jack","CBC",400,220,52)
# book3 = Book("3333333333","learn maths","john","xyz",500,300,45)
# book4 = Book("4444444444","learn biology","jack","xyz",400,200,78)


# lisst = [book1,book2,book3,book4]
# t = [i.title for i in lisst if i.author=="jack" ]
# print(t)
# # jack = [i[1] for i in lisst if i[2]=="jack"]
# for i in lisst:
#     t = i.display()
#     print(t)
# print(book1.display())
# book1.price_set = 100




# class Fraction:
#     def __init__(self,nr,dr=1):
#         self.nr = nr
#         self.dr = dr
#         if self.dr < 0:
#             self.nr*=-1
#             self.dr*=-1
#         self._reduce()

#     def show(self):
#         return print(f'{self.nr}/{self.dr}')
    
#     def __mul__(self,other):
#         if isinstance(other,int):
#             other = Fraction(other)
#         f = Fraction(self.nr * other.dr , self.dr * other.dr)
#         f._reduce()
#         return f
    
#     def __add__(self,other):
#         if isinstance(other,int):
#             othre = Fraction(other)
#         f = Fraction(self.nr * other.dr + other.nr * self.dr , self.dr * other.dr)
#         f._reduce()
#         return f
#     def __sub__(self,other):
#         if isinstance(other,int):
#             othre = Fraction(other)
#         f = Fraction(self.nr * other.dr - other.nr * self.dr , self.dr * other.dr)
#         f._reduce()
#         return f

#     @staticmethod
#     def hcf(x,y):
#         # print(x,y)
#         x = abs(x)
#         y = abs(y)
#         smaller = y if x>y else x
#         s = smaller 
#         while s>0:
#             if x%s==0 and y%s==0:
#                 break
#             s-=1
#         return s
    
#     def _reduce(self):
#         # return f'{self.nr/self.hcf(self.nr,self.dr)}/{self.dr/self.hcf(self.nr,self.dr)}'
#         h = Fraction.hcf(self.nr,self.dr)
#         if h == 0:
#             return 
#         self.nr //=h
#         self.dr //=h
            
# t = Fraction(2,3)
# j = Fraction(3,4)
# k = t.__add__(j)
# k.show()
# a = t-j
# a.show()



# class Product():
#     def __init__(self,id,marked_price,discount):
#         self.id = id
#         self.marked_price = marked_price
#         self._discount = discount

#     def display(self):
#         print(self.id,self.marked_price , self.discount)

#     @property
#     def discount(self):
#         return self._discount
    
#     @discount.setter
#     def set_discount(self,price):
#         if self.marked_price > 500:
#             self._discount += price
#         return print(self._discount)

#     @discount.getter
#     def get_price(self):
#         percent_value = (self.marked_price*self.discount)/100
#         return print(self.marked_price - percent_value)


# p1 = Product('adsf',650,50)
# p2 = Product('aasdf',33,891)
# p3 = Product('er',89,510)
# p4 = Product('xzcg',45,1)
# p1.get_price
# p1.set_discount=2
# p1.get_price


# class Circle():
    
#     def __init__(self,radius) -> None:
#         if radius < 0:
#             raise ValueError("radius can not be negative")
#         self.radius = radius
#         self._diameter = 2 * radius
#         self._circumference = 2*3.14*radius

#     @property 
#     def diameter(self):
#         return print(self._diameter)
    

#     @property
#     def circumference(self):
#         return print(self._circumference)

#     def area(self):
#         area = 3.14*self.radius*self.radius
#         return print(area)


# t = Circle(5)

# t.diameter
# t.circumference
# t.area()
    


###########################################################################




# class Salesperson:
#     total_avenue = 0
#     names = []
#     def __init__(self,name,age) -> None:
#         self.name= name
#         self.age = age
#         self.sales_amount = 0
#         Salesperson.names.append(self.name)

#     def make_sale(self,money):
#         self.sales_amount +=money
#         Salesperson.total_avenue += money
    
#     def show(self):
#         print(f'{self.name} {self.age} { self.sales_amount}')


# s1 = Salesperson('Bob',25)
# s2 = Salesperson('Ted',22)
# s3 = Salesperson('Jack',27)

# s1.make_sale(1000)
# s1.make_sale(1200)
# s2.make_sale(5000)
# s3.make_sale(3000)
# s3.make_sale(8000)

# s1.show()
# s2.show()
# s3.show()

# print(Salesperson.total_avenue)
# print(Salesperson.names)


#################################################################################


# class Employee:
#     domains = set()
#     allowed_domains = {'yahoo.com','gmail.com','outlook.com'}

#     def __init__(self,name,email) -> None:
#         self.name = name
#         self.email = email
#         t , domain = self.email.split('@')
#         if domain not in Employee.allowed_domains:
#             raise ValueError("This domain is not allowed")
#         Employee.domains.add(domain)
        
#     def display(self):
#         print(self.name,self.email)

# e1 = Employee('john','john@gmail.com')
# e2 = Employee('jack','jack@yahoo.com')
# e3 = Employee('jill','jill@outlook.com')
# e4 = Employee('Ted','Ted@yahoo.com')
# e5 = Employee('Tim','Tim@gmail.com') 
# e6 = Employee('Mike','Mike@yahoo.com')

# print(Employee.domains)


#####################################################################################

# class Stack:
#     MAX_SIZE = 10

#     def __init__(self) -> None:
#         self.items = []
 
#     def is_empty(self):
#         return self.items == []
    
#     def size(self):
#         return len(self.items)

#     def push(self,item):
#         if len(self.items)>=Stack.MAX_SIZE:
#             raise RuntimeError("Stack limit exceeded")
#         self.items.append(item)

#     def pop(self):
#         if self.is_empty():
#             raise RuntimeError("stack is empty")
#         return self.items.pop()
    
#     def display(self):
#         print(self.items)

# if __name__=="__main__":
#     st = Stack()
#     while True:
#         print("1.Push")
#         print("2.Pop")
#         print("3.Peek")
#         print("4.Size")
#         print("5.Display")
#         print("6.Quit")

#         choice = int(input("enter your choice : "))
#         if choice == 1:
#             x = int(input("enter the element to be pushed : "))
#             st.push(x)
#         elif choice == 2:
#             x = st.pop()
#             print("Popped element is : ",x)
#         elif choice==3:
#             print("Element at the top is : ", st.peek())

#         elif choice ==4:
#             print("Size of stack :",st.size())

#         elif choice == 5:
#             st.display()
#         elif  choice == 6 :
#             break
#         else:
#             print("Wrong choice")
#         print()


# t = Stack(2)


##############################################################################


# class BankAccount:
#     bank_name = "Punjab National Bank"
#     def __init__(self,name,balance=0) -> None:
#         self.name = name
#         self.balance = balance 
#         self.bank = BankAccount.bank_name

#     def display(self):
#         print(f'{self.name} {self.balance} {self.bank}')

#     def withdraw(self,amount):
#         self.balance -= amount

#     def deposit(self,amount):
#         self.balance+=amount

# a1 = BankAccount('Mike',45)
# a2 = BankAccount('Tom')
# a1.display()
# a2.display()



# class Time:
#     def __init__(self,h,m,s):
#         self._h = h
#         self._m = m
#         self._s = s

#     @property
#     def hour(self):
#         return self._h
#     @property
#     def minutes(self):
#         return self._m
#     @property
#     def seconds(self):
#         return self._s

#     def __eq__(self,other):
#         return True if _cmp(self,other)==0 else False
#     def __lt__(self,other):
#         return True if _cmp(self,other)==1 else False
#     def __le__(self,other):
#         return True if (_cmp(self,other)==0 or _cmp(self,other)==1) else False

# def _cmp(time1,time2):
#     if time1._h<time2._h:
#         return 1
#     if time1._h>time2._h:
#         return -1
#     if time1._m<time2._m:
#         return 1
#     if time1._m>time2._m:
#         return -1 
#     if time1._s<time2._s:
#         return 1
#     if time1._s>time2._s:
#         return -1
#     return 0

    
# t1 = Time(13,10,5)
# t2 = Time(5,15,30)
# t3 = Time(5,15,30)
# print(t1<t2)
# print(t1>t2)
# print(t1 == t2)
# print(t2==t3)
# print(t1<=t2)


class Length:
    def __init__(self,feet,inches):
        self.feet = feet
        self.inches = inches
    def __str__(self):
        return f'{self.feet} {self.inches}'
    def add_length(self,L):
        f = self.feet + L.feet
        i = self.inches + L.inches
        if i>=12:
            i = i-12
        f+=1
        return Length(f,i)
    def add_inches(self,inches):
        f = self.feet+inches // 12
        i = self.inches + inches %12
        if i>=12:
            i = i-12
        f+=1
        return Length(f,i)
    def __add__(self,other):
        if isinstance(other,int):
            return self.add_inches(other)
        return self.add_length(other)
        # return self+other
    def __radd__(self,other):
        return self.__add__(other)
length1 = Length(2,10)
length2 = Length(3,5)
print(length1+length2)
print(length1+2)
print(length1+20)
print(20+length1)


