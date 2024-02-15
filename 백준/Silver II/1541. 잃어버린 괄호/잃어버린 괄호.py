expression = input().split('-')
min_total = 0
for i in expression[0].split('+'):
    min_total += int(i)
for i in expression[1:]:
    for j in i.split('+'):
        min_total -= int(j)
print(min_total)