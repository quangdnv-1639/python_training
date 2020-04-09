# Arithmetic Operators
print(1 + 2.0)
print(2*3, 2*3.5)
print(20%3, 20%3.5)
print(25/6, 25/6.5)
print(12//5, 12//5.3)
print(3**2)

# Comparison Operators
print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)
print(1 == 2)
print(1 != 2)

# Assignment Operators
num1 = 123
print(num1)

num1+=3
print(num1)

num1-=2
print(num1)

num1*=4
print(num1)

num1/=7
print(num1)

num1%=5
print(num1)

# Logical Operators

if num1%2 == 0 and num1 > 0:
  print('and logical operators')
elif type(num1) == float or num1 == 2:
  print('or logical operators')

if not type(num1) == str:
  print('not logical operators')