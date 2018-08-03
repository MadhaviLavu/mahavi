n,k=input().split()
n=int(n)
k=int(k)
a = [int(x) for x in input().split()]
s=0
for i in range(0,k):
    s+=a[i]
print(s)
