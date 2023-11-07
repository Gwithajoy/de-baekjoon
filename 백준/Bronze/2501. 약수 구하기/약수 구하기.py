n, k = map(int, input().split())

lst =[]
for i in range(1, n+1):
  if n % i ==0:
    lst.append(i)
lst = sorted(lst)
if len(lst) <= k-1:
  print(0)
else:
  print(lst[k-1])