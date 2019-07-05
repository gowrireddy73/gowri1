m = int(input())
lis = list(map(int,input().split()))
lis.sort()
n= []
for i in range(len(lis)-1):
if lis[i]==lis[i+1]:
n.append(lis[i])
if n:
for x in set(n):
print( x, end=" ")
else 
print('unique')
