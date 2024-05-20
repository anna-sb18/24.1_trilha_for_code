import math

n = 2
soma = 0

while True:
    soma += 1/(n*(math.log(n)**2))
    print(soma)
    n += 1