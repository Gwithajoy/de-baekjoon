T = int(input())

for i in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    c = a + b
    print(f"Case #{i+1}:", c)
