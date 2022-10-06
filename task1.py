
class Rectangle:
    def __init__(self, len = 1, wid = 1):
        self.__length = len
        self.__width = wid

    @property
    def length(self):
        return self.__length

    def set_len(self, len):
        if not(len > 0 and len < 20):
            raise ValueError("Len not in range [0,20]")
        if not (isinstance(len, (float, int))):
            raise TypeError("Len isn't a float")
        self.__length = len

    @property
    def width(self):
        return self.__width


    def set_wid(self, wid):
        if not (wid > 0 and wid < 20):
            raise ValueError("Wid not in range [0,20]")
        if not (isinstance(wid, (float, int))):
            raise TypeError("Wid isn't a float")
        self.__width = wid


    def Perimeter(self):
        return (self.width + self.length) * 2


    def Area(self):
        return self.width * self.length


x = Rectangle(10.0, 10.0)
print(x.Area())
print(x.Perimeter())