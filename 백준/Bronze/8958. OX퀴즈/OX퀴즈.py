num = int(input())

for _ in range(num):
  lst = list(input())
  score = 0
  total = 0
  for n in lst:
    if n == "O":
      score += 1
      total += score
    else:
      score = 0
  print(total) 

