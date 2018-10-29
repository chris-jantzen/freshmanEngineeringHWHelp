from HW8_1_Task1_jantzeca import parallelResistance, seriesResistance

print('Enter 2 resistance values to be calculated:')
firstResistance = float(input('First value: '))
secondResistance = float(input('Second value: '))

print(firstResistance, secondResistance)

parallelTest = parallelResistance(firstResistance, secondResistance)
seriesTest = seriesResistance(firstResistance, secondResistance)

print('Parallel network type: ', parallelTest)
print('Series network type: ', seriesTest)