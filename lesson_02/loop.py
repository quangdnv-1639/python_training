# while
index = 0
while index <= 10:
  print(index)
  index+=1
else:
  print('index greater than 10')

# room = 0
# while room == 0:
#   chat = input('Enter room number: ')
#   print('Room name is: ', chat)         # Ctrl + C to exit

# for
str1 = 'Python!'
for i in str1:
  print(i)

arr1 = [1, 'two', 3.0, 'four']
for i in arr1:
  print(i)

for i in range(len(arr1)):
  print(arr1[i])

for i in range(1,100):
  sum1 = 0
  for j in range(1,i):
    if (i%j == 0):
      sum1+=j
  if i == sum1:
    print(i)
else:
  print('There are two perfect numbers in here')

# break
for letter in 'There are two perfect numbers in here':
  if letter == 'w':
    break
  print(letter)

# continue
for letter in 'There are two perfect numbers in here':
  if letter == 'w':
    continue
  print(letter)

# pass
for letter in 'There are two perfect numbers in here':
  if letter == 'w':
    pass
    print('pass code block')
  print(letter)