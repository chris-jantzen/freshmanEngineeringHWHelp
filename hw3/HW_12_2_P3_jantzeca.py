from random import randint

# P(Win) = 2/6 = 1/3
# P(Loss) = 4/6 = 2/3

roll = -1

numRolls = [10, 100, 1000, 10000, 100000, 1000000]
wins = [0, 0, 0, 0, 0, 0]
index = 0
for num in numRolls:
  for i in range(num):
    roll = randint(1, 6)
    if roll >= 5:
      wins[index] += 1
  index += 1

index = 0
for num in numRolls:
  print('For', num, 'Rolls')
  numWins = wins[index]
  print('Percent Wins:', (numWins/num) * 100)
  print('Percent Losses:', ((num-numWins)/num) * 100)
  index += 1
  