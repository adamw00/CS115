import random

class Die():
    
    def __init__(self):
        self.faceValue = 1
        self.MAX = 6

    def roll(self):
        '''Sets self.faceValue to a random integer from 1 to MAX
            Also returns that value'''
        #TODO
        value = random.randint(1,self.MAX)
        self.setFaceValue(value)
        return value

    def setFaceValue(self, faceValue):
        '''Setter for faceValue'''
        if(faceValue > 0 and faceValue <= self.MAX):
            self.faceValue = faceValue

    def getFaceValue(self):
        '''Getter for faceValue'''
        return self.faceValue

    def __str__(self):
        '''String representation of the current die value'''
        #TODO
        return str(self.faceValue)
