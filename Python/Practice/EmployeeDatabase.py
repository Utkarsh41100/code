class EmployeeDatabase():
   def __init__(self,Mylist):
     self.employee=[]
     self.employee.append(Mylist)
   def remove(self):
      i=input("Enter the index of employee whose data you want to delete:")
      del self.employee[i]  
   def Display() 

