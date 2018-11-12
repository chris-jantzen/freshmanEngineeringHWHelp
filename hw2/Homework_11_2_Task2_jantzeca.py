
resistors = input('Input resistor values:\n').split()
for i in range(len(resistors)):
  resistors[i] = float(resistors[i])

voltage = float(input('Input voltage:\n'))
seriesOrParallel = int(input('Series or parallel (0 or 1):\n'))

""" Series """
def seriesResistance(firstRes, secondRes):
	return firstRes + secondRes

def seriesVoltage1(voltageSource, firstRes, secondRes):
  return (firstRes/(firstRes+secondRes)) * voltageSource

def seriesVoltage2(voltageSource, firstRes, secondRes):
  return (secondRes/(firstRes+secondRes)) * voltageSource

def seriesCurrent(voltageSource, totalRes):
  return voltageSource / totalRes

""" Parallel """
def parallelResistance(firstRes, secondRes):
	invRTotal = (1/firstRes) + (1/secondRes)
	return 1/invRTotal

def parallelCurrentSource(voltageSource, totalRes):
  return voltageSource/totalRes

def parallelCurrent1(firstRes, secondRes, currentSource):
  return (secondRes/(firstRes+secondRes)) * currentSource

def parallelCurrent2(firstRes, secondRes, currentSource):
  return (firstRes/(firstRes+secondRes)) * currentSource

# If series
if seriesOrParallel == 0:
  totalResistance = seriesResistance(resistors[0], resistors[1])
  voltage1 = seriesVoltage1(voltage, resistors[0], resistors[1])
  voltage2 = seriesVoltage1(voltage, resistors[0], resistors[1])
  current = seriesCurrent(voltage, totalResistance)
  print('Total Resistance = {}'.format(totalResistance))
  print('Voltage 1 = {}'.format(voltage1))
  print('Voltage 2 = {}'.format(voltage2))
  print('Current = {}'.format(current))

# If parallel
if seriesOrParallel == 1:
  totalResistance = parallelResistance(resistors[0], resistors[1])
  currentSource = parallelCurrentSource(voltage, totalResistance)
  current1 = parallelCurrent1(resistors[0], resistors[1], currentSource)
  current2 = parallelCurrent2(resistors[0], resistors[1], currentSource)
  parallelVoltage = voltage # V1 = V2 = Vs
  print('Total Resistance = {}'.format(totalResistance))
  print('Current Source = {}'.format(currentSource))
  print('Current 1 = {}'.format(current1))
  print('Current 2 = {}'.format(current2))
  