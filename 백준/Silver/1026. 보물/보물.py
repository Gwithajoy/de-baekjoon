N = int(input())

for i in range(2):
  if i+1 == 1 :
    lst1 = list(map(int, input().split()))
  else:
    lst2 = list(map(int,input().split()))


lst1.sort()
lst2.sort(reverse=True)

total = 0
for j in range(N):
    total += (lst1[j] * lst2[j])
print(total)