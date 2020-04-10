import os

file = open('name.txt', 'w')
file.write('Nguyen Van Quang')
file.close()

with open('name.txt', 'w') as file:
  file.write('Nguyen Van Duong')
  file.close()

with open('name.txt', 'r') as file:
  print(file.read())

os.mkdir('folder_test')
os.rmdir('folder_test')
os.getcwd()