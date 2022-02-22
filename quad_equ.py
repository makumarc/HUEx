import cmath

a=int(input("a= "))

b=int(input("b= "))

c=int(input("c= "))

d = (b**2) - (4*a*c)

solu_1 = (-b-cmath.sqrt(d))/(2*a)

solu_2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(solu_1,solu_2)) 