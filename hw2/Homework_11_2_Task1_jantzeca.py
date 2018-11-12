import math

indeciesOfRefraction = input('Enter indices of refraction for bottom two media:\n').split()
if len(indeciesOfRefraction) != 2:
  print('Need two indecies of refraction')
elif indeciesOfRefraction[0] > indeciesOfRefraction[1]:
  print('Error, no refraction in the second media')
  exit()

for i in range(len(indeciesOfRefraction)):
  indeciesOfRefraction[i] = float(indeciesOfRefraction[i])

angleOfIncidence = float(input('Enter angle of incidence (in degrees):\n'))

distances = input('Enter d1 and d2 (units):\n').split()
if len(indeciesOfRefraction) != 2:
  print('Need two distances')

for i in range(len(distances)):
  distances[i] = float(distances[i])

# n1 sin1(theta1) = n2 sin2(theta2)
def getTheta2(n1, n2, theta1):
  return math.degrees(math.radians(90) - math.asin((n1 * math.sin(math.radians(theta1))/n2)))

def getBottomLength(d, theta):
  return d * math.tan(math.radians(theta))

theta2 = getTheta2(indeciesOfRefraction[0], indeciesOfRefraction[1], angleOfIncidence)
print('theta2: {}'.format(theta2))
length1 = getBottomLength(distances[0], angleOfIncidence)
print('length1: {}'.format(length1))
length2 = getBottomLength(distances[1], theta2)
print('length2: {}'.format(length2))
d3 = length1 + length2
print(d3)
