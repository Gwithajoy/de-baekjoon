find_s = list(input())
letters ='abcdefghijklmnopqrstuvwxyz'

for l in letters:
  if l in find_s:
    print(find_s.index(l), end = ' ')
  else:
    print(-1, end = ' ')

