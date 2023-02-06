def solve(numheads, numlegs):
    d = dict()
    z = (numlegs - 2 * numheads) / 2
    k = numheads - z
    d['zaicev'] = z
    d['kur'] = k
    return d



numheads = 35
numlegs = 94
print(solve(numheads,numlegs))

