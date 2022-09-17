from calculator import Calculator
from config import Config
import numpy as np

u = Config()
c = Calculator("This is a calculator")

print(u.username)
print(u.password)
print(c.text)
print(c.add(2,3))
print(c.subtract(3,2))
print(c.getSin(np.pi/2))