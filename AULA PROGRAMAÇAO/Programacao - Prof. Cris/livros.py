livro = int(input ("Digite o valor de copias do livro:"))
desconto = 35 / 100
transporte = 3
transpadicional = 3 + 0.75
copia = int(input ("Digite o valor da quantidade de copias:"))
custolivro = livro - (livro * desconto) + transporte
custoadicional = livro - (livro * desconto) + transpadicional
total = custolivro + (custoadicional * copia)
print ("VALOR FINAL DOS LIVROS:", total)
