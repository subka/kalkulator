import math
dane = input().split()

n = int(dane[0])
k = int(dane[1])

if k == 1 or k == n:
    print(1)
else:
    if k > n:
        print(0)
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        wynik = a // (b*math.factorial(n-k))
        print(wynik)
