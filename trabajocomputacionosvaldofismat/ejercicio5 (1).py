numero=int(input("ingresa los segundos: "))
d=(int(numero/86400))
h=(int((numero-(d*86400))/3600))
m=(int((numero-(d*86400)-(h*3600))/60))
s=(int((numero-(d*86400)-(h*3600)-(m*60))))
print(str(d)+"d "+str(h)+"h "+str(m)+"m "+str(s)+" s")
