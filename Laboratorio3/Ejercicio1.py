import math

print "Hola Bienvenido"

latitud1=float(input("Ingrese la primer latitud: "))
longitud1=float(input("Ingrese la primer longitud: "))
latitud2=float(input("Ingrese la segunda latitud: "))
longitud2=float(input("Ingrese la segunda longitud: "))

def distancia(x1,y1,x2,y2):
	x1=(x1*math.pi)/180
	y1=(y1*math.pi)/180
	x2=(x2*math.pi)/180
	y2=(y2*math.pi)/180
        return x1,y1,x2,y2

def dis(x1,y1,x2,y2):
    d=6371.01*math.acos((math.sin(gar(x1,y1,x2,y2)[0]))*(math.sin(gar(x1,y1,x2,y2)[2]))+((math.cos(gar(x1,y1,x2,y2)[0]))*(math.cos(gar(x1,y1,x2,y2)[2]))*(math.cos((gar(x1,y1,x2,y2)[1])-(gar(x1,y1,x2,y2)[3])))))
    return d

print "La distancia entre los dos puntos es: ", dis(latitud1,longitud1,latitud2,longitud2), +str" kilometros"
