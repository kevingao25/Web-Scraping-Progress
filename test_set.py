U = set()
S = set()
T = set()

for n in range(-37, 37):
    if n == 0:
        U.add(n)
    elif (36 % n == 0):
        U.add(n)

for s in U:
    if (s * s) in U:
        S.add(s)

for t in U:
    if t == 1:
        T.add(t)
    elif 8 % (t-1) == 0:
        T.add(t)

print("The universal set U is: ", U)
print("The set S is: ", S)
print("The set T is :", T)

union = S.union(T)
print("union: ",union)
intersection = S & T
print("intersection: ", intersection)
difference = T - S
print("difference: ", difference)
complement = U - S
print("complement: ", complement)

