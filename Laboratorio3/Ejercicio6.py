print "Programa que transforma la longevidad humana en perruna"

anospersona=int(raw_input("Ingrese los de anos persona: "))
if anospersona<0:
	anospersona=int(raw_input("Ingrese un numero positivo: "))
else:
	pass

def conversion(a):
	a=0
	for i in range(1,a+1):
		if i<=2:
			a=a+10.5
		else:
			a=a+4
	return a

print conversion(anospersona)
