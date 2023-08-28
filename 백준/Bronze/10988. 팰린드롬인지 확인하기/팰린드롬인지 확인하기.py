letter = input()
backward = letter[-1:-(len(letter)+1):-1]

if letter == backward:
  print(1)
else:
  print(0)