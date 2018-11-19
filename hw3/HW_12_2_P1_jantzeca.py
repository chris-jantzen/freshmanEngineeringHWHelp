# P(n)=P(n-2)+P(n-3)

# Initial Conditions
# P(0)=3,P(1)=0,P(2)=2
P = [3, 0, 2]

inputNumber = int(input('Enter a real positive integer:\n'))
for i in range(3, inputNumber+1):
  P.append(P[i-2] + P[i-3])

print(P)
