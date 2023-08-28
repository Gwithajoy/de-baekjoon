word = input().lower()
a = list(set(word))

dct = {}
for i in range(len(a)):
    b = a[i]
    c = word.count(b)
    dct[b] = c

max_values = max(dct.values())
max_keys = [key for key, values in dct.items() if values == max_values]

if len(max_keys)==1:
  print(max_keys[0].upper())
else:
  print("?")