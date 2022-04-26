import Die as Die

class DiceQuad():

    def __init__(self):
        '''Initilizes dieList as a list of 4 Die objects
            To create a die object, call Die()'''
        self.dieList = [Die.Die(),Die.Die(),Die.Die(),Die.Die()]

    def roll(self):
        '''Rolls all four dice in dieList'''
        #TODO
        for x in self.dieList:
            x.roll()
            
    
    def num1s(self):
        '''return the number of ones rolled'''
        #TODO
        roll = [self.dieList[0].getFaceValue(),
                self.dieList[1].getFaceValue(),
                self.dieList[2].getFaceValue(),
                self.dieList[3].getFaceValue()]
        if roll.count(1) == 4:
            return 4
        if roll.count(1) == 3:
            return 3
        if roll.count(1) == 2:
            return 2
        if roll.count(1) == 1:
            return 1
        if roll.count(1) == 0:
            return 0
    
    
    def getDiceTotal(self):
        '''return the sum of the dice'''
        #TODO
        return self.dieList[0].getFaceValue()+self.dieList[1].getFaceValue()+self.dieList[2].getFaceValue()+self.dieList[3].getFaceValue()

    def __str__(self):
        '''String representation of the dice roll'''
        s = "("+str(self.dieList[0])
        for x in range(1, len(self.dieList)):
            s = s+","+str(self.dieList[x])
        s = s+")"
        return s
