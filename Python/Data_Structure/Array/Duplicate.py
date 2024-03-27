
# arr=[1,2,3,4,1,2,3,4,1,2,3,4]
# length=len(arr)
# for i in range(length-1):
#     for j in range(length-1):
#         temp=0
#         if arr[j]<arr[j+1]:
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp
# j=0          
# print(arr)
# while j<(len(arr)-1):
#     if arr[j]==arr[j+1]:
#         arr.pop(j+1)
#     else: j+=1
# print(arr)
arr=[1,2,3,4,1,2,3,4,1,2,3,4]
def dup(arr):
    if not arr:
        return 0
    arr.sort()
    j=0
    for i in range(len(arr)-1):
        if arr[i]!=arr[j]:
            j+=1
        else:
            arr[j]=arr[i]
    return j+1,arr[:j+1]
range,array=dup(arr)
print(range,array)            