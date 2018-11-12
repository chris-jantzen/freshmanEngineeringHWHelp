
def parallelResistance(firstRes, secondRes):
  invRTotal = (1/firstRes) + (1/secondRes)
  rTotal = 1/invRTotal
  return rTotal

def seriesResistance(firstRes, secondRes):
  rTotal = firstRes + secondRes
  return rTotal


# How to make these one line, but a little less readable
# so I wouldn't use these in your homework, but it's worth
# seeing anyway for understanding how you really should be
# thinking when writing code. (More the parallel one than the other)
def howParallelShouldLook(firstRes, secondRes):
  return (firstRes**-1 + secondRes**-1)**-1

def howSeriesResistanceShouldLook(firstRes, secondRes):
  return firstRes+secondRes