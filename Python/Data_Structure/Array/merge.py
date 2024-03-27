arr1=[21,33,4,5,6]
arr2=[14,27,31,4,5]
arr3=[]
j=0
i=0
while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1  
print(arr3)            