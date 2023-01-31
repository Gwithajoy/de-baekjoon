x = int(input())
lst= list(map(int,input().split()))

k = 0
z = max(lst)
for i in range(len(lst)):
  j = (lst[i]/z)*100
  k += j
print(k/len(lst))

 