lst_x = []
y = [lst_x.append(x) for x in range(1,31)]

lst = []
for _ in range(28):
  z = int(input())
  lst.append(z)

i = set(lst_x) - set(lst)
print(min(i))
i.remove(min(i))
print(min(i))
