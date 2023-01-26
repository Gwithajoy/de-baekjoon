lst = []
for _ in range(9):
  i = int(input())
  lst.append(i)

print(max(lst))
print(lst.index(max(lst))+1)
