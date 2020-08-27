''' najst v tom dlhom subore male pismena obkolesene prave 3 velkymi. a z nich je sprava '''

import re
import string

myfile = (open('textak.txt', "r"))
T = myfile.read()

V = re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', T)

for l in V:
    print(l, end = "")
    


# text is in t2
markers = ''.join(['0' if c.islower() else '1' for c in T])
     
def f( res, T, markers ):
    n = len(markers.partition('011101110')[0])
    return f( res+T[n+4], T[n+9:], markers[n+9:] ) if n != len(markers) else res
print f( '', t2, markers )