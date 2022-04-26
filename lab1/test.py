import random
def rollDie():
  '''rolls a single die (wow)'''
  return random.randint(1,6)

# TODO
def rollDice():
  '''grabs the roll for four dice'''
  rolls = []
  for x in range(4):
    rolls.append(rollDie())
  return rolls
