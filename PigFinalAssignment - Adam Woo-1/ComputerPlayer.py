from pigPlayer import PigPlayer

class ComputerPlayer(PigPlayer):

    gotAllOnes = False

    def __init__(self, owner, name, target=20):
        PigPlayer.__init__(self, owner, name)
        self.targetPointsPerRound = target

    def wantsHandOver(self):
        '''Return boolean if the AI wants to end the round based on target'''
        #TODO
        if self.roundScore + self.score >= PigPlayer.WINNING_SCORE:
            return True
        if self.roundScore < self.targetPointsPerRound:
            return False
        else:
            return True
