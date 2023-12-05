x_lst =[]
y_lst =[]
num = int(input())
for _ in range(num):
  x,y = input().split()
  x_lst.append(int(x))
  y_lst.append(int(y)) 

print((max(x_lst)- min(x_lst)) * (max(y_lst)- min(y_lst)))