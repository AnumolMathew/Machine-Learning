#21MCA007
#Anumol Mathew

n1 = int(input("enter first number :"))
n2 = int(input("enter second number :"))
flag=0


for i in range(2,n2):
    if (n2 % i == 0) & (n1 % i == 0):
        flag=1
        break

if flag == 1:
    print("numbers {} & {} aren't co-prime".format(n1, n2))
else:
    print("numbers {} & {} are co-prime".format(n1, n2))


