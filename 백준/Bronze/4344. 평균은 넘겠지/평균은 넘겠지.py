num = int(input())
score_lst = []


for n in range(num):
  score = list(map(int, input().split()))
  avrg = sum(score[1:])/score[0]
  student = 0
  for i in score[1:]:
    if avrg < i:
      student += 1
  rate = student/score[0] * 100
  print(f'{rate:.3f}%')