N = int(input())
withdraw_time = list(map(int,input().split()))
withdraw_time.sort()

all_time_lst = []
spent_time = 0
for i in withdraw_time:
  spent_time += i
  all_time_lst.append(spent_time)
print(sum(all_time_lst))