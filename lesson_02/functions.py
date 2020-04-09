import math

def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n))):
    if n % i ==0:
      return False
  return True

def info(name, address, gender='Male'):
  return 'Name:', name, 'address: ', address, 'gender: ', gender

def classInfo(name, class_room, *color):
  info = 'Name' + name + '\nClass room:' + class_room + '\nColor:'
  for i in range(len(color)):
    info += color[i] + ', '
  return info

num = int(input('Enter n to check: '))
if isPrime(num):
  print(num, 'is prime')
else:
  print(num, 'is not prime')

print(info('Quang', 'HaNoi'))
print(info('Lan', 'HaNoi', 'Female'))

square = lambda x, y: x*y

print(classInfo('clound', 'sky', 'red', 'green'))
print(square(2, 3))
