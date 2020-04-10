import random
import string

def printRandomBookName(length):
  letters = string.ascii_letters
  return ' '.join((random.choice(letters)) for i in range(length))
