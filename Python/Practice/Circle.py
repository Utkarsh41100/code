class circle():
    def __init__(self,Radius):
        self.Radius=Radius
        self.Area=3.14*self.Radius*self.Radius
        self.Circumference=2*3.14*self.Radius
    def showdata(self):
        print(f"The Area of circle with radius  {self.Radius} is {self.Area} and it's Circumference is {self.Circumference}")
a=circle(7) 
a.showdata()   