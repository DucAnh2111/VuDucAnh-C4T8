# In ra 1 so ngau nhien tu 1-100 / hint: random in python 3
from random import randint

a = randint(0, 100)
print(a)

if a < 30:
    print("Rainy")
if 30 <= a < 60:
    print("Cloudy")
if a >= 60:
    print("Sunny")