idades = []

for i in range(20):
    idade = int(input(f"Digite a {i+1}ª idade: "))
    idades.append(idade)

maior_idade = max(idades)
menor_idade = min(idades)
print(f"A maior idade é: {maior_idade}")
print(f"A menor idade é: {menor_idade}")