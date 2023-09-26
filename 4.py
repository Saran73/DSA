def order_rev(x):
    x.reverse()
    print(x)

x = []
n = int(input("enter the length: "))
for i in range(0,n):
    k=int(input("enter the elements: "))
    x.append(k)
    print(x)

order_rev(x)


def order_rev():
    return X[::-1]
    print(X)

n = int(input())
Y = input()
X = Y.split()
reverse_ver = order_rev()
print(*reverse_ver)


a_score=0
b_score=0
a=input().split()
b=input().split()
for i in range (len(a)) :
    if(a[i]>b[i]):
        a_score+=1
        b_score+=0
    elif(a[i]<b[i]):
        b_score+=1
        a_score+=0
    else:
        b_score+=0
        a_score+=0
print( a_score , b_score)

def aVeryBigSum(ar):
    summ = 0
    for i in range(len(ar)):
        summ += ar[i]
    return summ


ar = input().split()
result = aVeryBigSum(ar)
print(result)