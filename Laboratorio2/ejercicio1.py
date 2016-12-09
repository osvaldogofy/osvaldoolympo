import math
cat1=float(input("escriba el primer cateto"))
cat2=float(input("escriba el segundo cateto"))
def obtener(a,b):
    hipotenusa=float
    hipotenusa=math.sqrt((a*a)+(b*b))
    return hipotenusa
print "La hipotenusa del triangulo con catetos: " ",cat1," y ",cat2," es: ",obtener(cat1,cat2)
