num = int(input('Enter your number: '))

for i in range(num+1):
  square = i*i
  if square >= num:
    print(f'{i} --- {square}')