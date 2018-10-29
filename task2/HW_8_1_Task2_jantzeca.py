def commandLineTool():
  lastName = input('Enter your last name:\n')
  firstName = input('Enter your first name:\n')
  ageInYears = int(input('Enter your age in whole years:\n'))
  daysSinceBirthday = int(input('Enter the days elapsed since your last birthday:\n'))
  printResults(lastName, firstName, ageInYears, daysSinceBirthday)

def printResults(lastName, firstName, wholeYears, daysSinceBirthday):
  print(firstName, lastName)
  preciseYears = calculateYears(wholeYears, daysSinceBirthday)
  print('You are {:.8} years old'.format(preciseYears))
  minutes = calculateAgeInMinutes(preciseYears)
  print('You are {} minutes old'.format(minutes))

def calculateYears(wholeYears, daysSinceBirthday):
  numDaysInYear = 365.242199
  years = wholeYears + daysSinceBirthday/numDaysInYear
  return years

def calculateAgeInMinutes(preciseYears):
  minutesPerFullRotation = 60*24*365.242199
  return int(preciseYears * minutesPerFullRotation)

commandLineTool()