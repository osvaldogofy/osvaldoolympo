peso = raw_input ('INTRODUCE PESO ACTUAL: ')
altura = raw_input ('INTRODUCE ALTURA ACTUAL EN CENTIMETROS: ')
imc = (float(peso)/(float(altura)*float(altura)))*10000

print 'Su IMC es: ', imc
if imc <16:
    raw_input ('DELGADEZ SEVERA')
if imc <16.99 and imc >16:
    raw_input ('DELGADEZ MODERADA')
if imc <24.99 and imc >18.5:
    raw_input ('NORMAL')
if imc >25:
    raw_input ('SOBREPESO')
