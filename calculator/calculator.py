import numpy as np

class Calculator:
    def __init__(self, text):
        self.text = text
    
    def add(self, n1, n2):
       return n1 + n2
    
    def subtract(self, n1, n2):
        return n1 - n2

    def getSin(self, n1):
        return np.sin(n1)