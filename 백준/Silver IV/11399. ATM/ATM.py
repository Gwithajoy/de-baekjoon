N = int(input())
withdraw_time = list(map(int, input().split()))
withdraw_time.sort()

total_time = 0
for i in range(N):
    total_time += withdraw_time[i] * (N - i)

print(total_time)