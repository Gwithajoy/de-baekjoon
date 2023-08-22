a = int(input())
for i in range(1, a+1):
    j= (2*i) -1
    b = a-i
    print(' ' * b+'*' * j)
for l in range(a-1, 0,-1):
    k= (2*l) -1
    c = a-l
    print(' ' * c+'*' * k)