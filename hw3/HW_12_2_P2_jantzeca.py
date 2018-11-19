saveMax = float(input('How much do you wish to save?: $')) * 100
balance = [1]
index = 0
dailyAddition = 2
while (balance[index] < saveMax):
  balance.append(balance[index] + dailyAddition)
  dailyAddition += 1
  index += 1

print('The final balance is: $', balance[index]/100)
# Subtract one from daily addition to offset the addition that was made in the last run of the while loop
print('Contribution on last day: $', (dailyAddition-1)/100)
numDays = len(balance)
print('Number of days to save: ', numDays)
print('Number of years to save: ', str(round(numDays/365, 2)))
