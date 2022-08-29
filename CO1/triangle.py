#21MCA007
#Anumol Mathew
print("21MCA007 Anumol Mathew")

n1 = int(input("enter the side1:"))
n2 = int(input("enter the side2:"))
n3 = int(input("enter the side3:"))
if n1 == n2 and n1 == n3:
   print("triangle is equilateral")
elif n1 == n2 or n2 == n3 or n1 == n3:
   print("triangle is isosceles")
else:
   print("triangle is scalar")

