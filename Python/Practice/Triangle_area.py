import math
class Triangle():
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.semiperi=(self.side1+self.side2+self.side3)/2
    def validation(self):
        if (self.side1<self.side3+self.side2) and (self.side2<self.side3+self.side1) and (self.side3<self.side1+self.side2):
            return True
        else:
            return False
    def area(self):
        return math.sqrt(self.semiperi*((self.semiperi-self.side1)+(self.semiperi-self.side2)+(self.semiperi-self.side3)))  
    def display(self):
        Calculated_area=self.area()
        print(f"The area of sides with {self.side1},{self.side2} and {self.side3} is {Calculated_area}")    
a=Triangle(3,4,5)        
if (a.validation):
    print("The triangle is valid")
a.display()    
