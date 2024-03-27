class Rectangle:
    def __init__(self,Length,Breadth):
        self.kength=Length
        self.treadth=Breadth

    def area(self):
        return self.kength*self.treadth 
    
    def perimeter(self):
        return 2*(self.kength+self.treadth)
 
a=Rectangle(7,8)
area=a.area()
perimeter=a.perimeter()
print(f"The area of rectangle is {area}")
print(f"The perimeter of rectangle is {perimeter}")