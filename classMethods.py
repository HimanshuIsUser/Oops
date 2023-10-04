#  class method 

class Myclass():
    a = 5
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        self.a = 10

    def callFunction(self):
        print(f'My name is {self.name} , I am {self.age} years old')

    @classmethod
    def main(cls):
        print(cls.a)

    @classmethod
    def makeobject(cls,name,age):
        return cls(name , age)


t = Myclass.makeobject('himanshu',45)
t.callFunction()