a = input()

lst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
d=0
for s in lst:
  for l in a:
    if l in s:
      b = int(lst.index(s))
      c = b+3
      d = d+c
print(d)
