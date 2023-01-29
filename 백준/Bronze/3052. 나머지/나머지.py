x = []
for i in range(10):
  y = int(input())
  z = y % 42
  x.append(z)
x = set(x)
print(len(x))
