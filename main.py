def sumoftwo(arr,target):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
        return [0]

arr=[]
n=int(input("enter the values"))
for i in range(0,n):
    k = int(input("elements of arrays"))
    arr.append(k)
print(arr)

target=int(input("enter the value:"))

print(sumoftwo(arr,target))

