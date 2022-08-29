print("21MCA007 Anumol Mathew")


import math
n1=int(input("enter the first num"))
n2=int(input("enter the second num"))
if math.gcd(n1,n2)==1:
    print("numbers {} & {} are co-prime".format(n1, n2))
else:
    print("numbers {} & {} aren't co-prime".format(n1, n2))