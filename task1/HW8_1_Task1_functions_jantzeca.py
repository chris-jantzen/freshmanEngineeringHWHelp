from HW8_1_Task1_jantzeca import parallelResistance, seriesResistance

print('Enter 2 resistance values to be calculated:')
firstResistance = int(input('First value: '))
secondResistance = int(input('Second value: '))

parallelTest = parallelResistance(firstResistance, secondResistance)
seriesTest = seriesResistance(secondResistance, secondResistance)

print('Parallel network type: ', parallelTest)
print('Series network type: ', seriesTest)