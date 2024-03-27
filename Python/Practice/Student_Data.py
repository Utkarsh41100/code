class student():
    def __init__(self,Name,Trade,Registration_Number):
        self.Name=Name
        self.Registration_Number=Registration_Number
        self.Trade=Trade

    def show_data(self):
        print(f"My name is {self.Name}")
        print(f"My Regitration number is {self.Registration_Number}")
        print(f"My Trade is {self.Trade}")

a=student("Utkarsh","CDE","2211009")
a.show_data()

