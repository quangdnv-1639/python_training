import sys

randomList = [1, 0, -2, 'a']
for i in randomList:
  try:
    print(1/int(i))
  except:
    print('Error', sys.exc_info()[0])

for i in randomList:
  try:
    print(1/int(i))
  except ValueError:
    print('ValueError')
  except ZeroDivisionError:
    print('ZeroDivisionError')

try:
  a = int(input("Enter a positive integer: "))
  if a <= 0:
    raise ValueError("That is not a positive number!")
except ValueError as error:
  print(error)

try:
  file = open('name.txt', 'w',  encoding = 'utf-8')
  file.write('Nguyen Van A')
finally:
  file.close()
