vfinal = float(input ("Valor final desejado:"))

i = float(input ("Rentabilidade em mensal:"))

i = i / 100

meses = int(input ("Numero de meses aplicaçao:"))

vinicial = vfinal / (1 + i) **meses

print (" valor iniciar para aplicação R$:", vinicial)
