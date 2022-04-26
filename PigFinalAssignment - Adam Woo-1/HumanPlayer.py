from pigPlayer import PigPlayer


class HumanPlayer(PigPlayer):

    gotAllOnes = False
    
    def wantsHandOver(self):
        '''Asks a human player if they want to play again'''
        
        print("\tYour current score: " + str(self.getCurrentScore()))
        print("\tRoll again? (yes or no) ")
        #TODO
        ans = input()
        while (ans != 'yes') and (ans!='no'):
            ans = input("\tRoll again? (yes or no) ")
        return True if ans=='no' else False
