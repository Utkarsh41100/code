january=[1,4,7,9,4,2,6,66,99,5,3,4,2,9,6]
february=[45,6,8,9,30,65,5,5,3,5,7,8,11,3,67]
extra=0
size=len(february)
for i in range(size):
    extra+=february[i]-january[i]
print(extra)    

