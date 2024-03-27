class Cars():
    def __init__(self,Model,Year,Company):
        self.Model=Model
        self.Year=Year
        self.Company=Company
        self.CurrentYear=2024
    def age(self):
        self.age=self.CurrentYear-self.Year
    def display(self):
        print(f"The Name of the company is {self.Company} it's model is {self.Model} it was sold in {self.Year} and now it's age is {self.age} Years")
a=Cars("Audi Q8",2018,"Audi")
a.age()
a.display()