
PV = float(input("Valor inicial que voce irá investir: "))

i = float(input(" Valor da rentabilidade mensal:"))
i = i / 100

n = int(input("quantidade de meses que o dinheiro ir´ficar aplicado:"))

juros = PV *(1 + i)** n
print ("O VALOR DO JUROS É DE:",juros)
