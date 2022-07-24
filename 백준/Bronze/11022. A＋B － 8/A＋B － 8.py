T = int(input())

for i in range(T):
    a, b = input().split()
    c = int(a) + int(b)
    print(f"Case #{i+1}:", a ,"+", b, "=", c)
