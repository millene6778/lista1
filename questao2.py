#QUESTÃO 2
numeros_reais = []

#Loop para ler 10 números reais
for i in range(10):
    numero = input(f"Digite o {i+1}º número real: ")
    numeros_reais.append(numero)

#Mostra os números na ordem inversa
print("Números na ordem inversa:")
for numero in reversed(numeros_reais):
 print(numero)