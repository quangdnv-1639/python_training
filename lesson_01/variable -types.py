# Assign values
# Single assign values
var1 = 1         # Integer
var2 = 2.0       # Float
var3 = 'three'   # String
print (var1, var2, var3)

# Multi assign values
var4 = var5 = var6 = 4.0
print (int(var4), float(var5), complex(var6))

var7, var8, var9 = 7, 8.7654321, 'nine'
print (var7, round(var8, 2), var9)

# Delete variable
del var1
# print(var1) #raise NameError: name 'var1' is not defined

# Number: example above

# Strings
str1 = 'Python language!'
print (str1)
print (str1[0])
print (str1[2:5])
print (str1[2:])
print (str1[:2])
print (str1 * 2)
print (str1 + '\nThat is greate!')
print ('P' in str1)
print ('P' not in str1)
print ('P' == 'p')
print ('P123' >= 'p12')

# Lists
list1 = ['one', 2 , 3.0, 'four', 5.0]
list2 = [6, 'seven']

print (list1)
print (list1[0])
print (list1[1:3])
print (list1[2:])
print (list2 * 2)
print (list1 + list2)

list1[0] = 1
print (list1)

list1.append(list2)
print (list1)

del list1[4]
print (list1)

# Tuples
tuples1 = ('one', 2 , 3.0, 'four', 5.0)
tuples2 = (6,) # syntax with a item

print (tuples1)
print (tuples1[0])
print (tuples1[1:3])
print (tuples1[2:])
print (tuples2 * 2)
print (tuples1 + tuples2)

# tuples1[0] = 1 # raise TypeError: 'tuple' object does not support item assignment

del tuples1 # Delete tuples, can't delete individual elements in tuples
# print (tuples1) # raise NameError: name 'tuples1' is not defined

# Dictionary
dic1 = {'one' : 1, 2.0 : 'two', 3 : 3.00, 'four' : 'four'}

print (dic1)
print (dic1['one'])
print (dic1[2.0])
print (dic1.keys())
print (dic1.values())

dic1[2.0] = 'two'
print (dic1)

del dic1['one']
print (dic1)

print (dic1.clear())

del dic1
# print (dic1) # rails NameError: name 'dic1' is not defined
