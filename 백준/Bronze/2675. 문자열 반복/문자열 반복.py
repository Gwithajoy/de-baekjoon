num = int(input())
letters = []
for _ in range(num):
  repeat = list(input().split())
  for r in str(repeat[1]):
    z = int(repeat[0]) * r
    letters.append(z)
    j = ''.join(letters)
  print(j)
  letters.clear()

