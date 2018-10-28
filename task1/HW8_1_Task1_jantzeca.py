
def parallelResistance(firstRes, secondRes):
  invRTotal = (1/firstRes) + (1/secondRes)
  rTotal = 1/invRTotal
  return rTotal

def seriesResistance(firstRes, secondRes):
  rTotal = firstRes + secondRes
  return rTotal

def howParallelShouldLook(firstRes, secondRes):
  return (firstRes**-1 + secondRes**-1)**-1

def howSeriesResistanceShouldLook(firstRes, secondRes):
  return firstRes+secondRes