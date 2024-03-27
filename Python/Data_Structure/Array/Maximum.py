arr=[1,2,3,4,5,6,77,8,3,2,1,4,5,6,7,7,2,8]
max=arr[0]
for i in range(len(arr)):
    if max<arr[i]:
     max=arr[i]
print(f"The maximum number is the array is {max}")


                    