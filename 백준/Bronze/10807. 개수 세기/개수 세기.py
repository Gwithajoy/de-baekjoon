x = map(int, input())
lst_x = list(map(int, input().split()))
y = int(input())
if y in lst_x:
  print(lst_x.count(y))
else: 
  print(0)