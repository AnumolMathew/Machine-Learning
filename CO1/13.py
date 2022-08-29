print("21MCA007 Anumol Mathew")
n = int(input("enter a positive number :"))

while n != 0:
    temp = n
    s = 0

    while n != 0:
        r = n % 10
        s = s + r
        n = n // 10

    print( "{} - {} =".format(temp,s),end=" ")
    n = temp - s
    print(n)