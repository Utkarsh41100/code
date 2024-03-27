arr=[1, 2, 3, 4, 5]
k=1
for j in range(k):
 first=arr[0]
 for i in range(len(arr)-1):
  arr[i]=arr[i+1]
 arr[-1]=first 

print(arr)    
