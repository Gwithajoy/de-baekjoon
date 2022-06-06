h,m = map(int, input().split())


if h > 0 and m < 45:
  print((h-1), (15 + m))
elif m >= 45:
  print( h , (m -45))
else:
  print(23, m + 15)


