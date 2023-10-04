class Rectangle:
    def __init__(self,length,breath) -> None:
        self.__length = length
        self.__breath = breath

    def getattr(self):
        return f'{self.__length} and {self.__breath}'
    
class Square(Rectangle):
    def __init__(self, length, breath) -> None:
        super().__init__(length, breath)

def print_shape_details(obj):
    if isinstance(obj,Square):
        area = obj.length*obj.length
        print(obj.length)
        parameter = obj.length*4
        return f'Area is : {area} and parameter is : {parameter}'
    if isinstance(obj,Rectangle):
        area = obj.length * obj.breath
        parameter = obj.length + obj.breath
        return f'Area is : {area} and parameter is : {parameter}'
    return print("This function works with only objects of Rectangle and Square class")

t = Rectangle(6,2)
print(t.getattr())
# t = Square(8)
# print(print_shape_details(t))

