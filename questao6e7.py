compras_do_mes = ["pão", "miojo", "biscoito", "feijão", "frutas", "azeitona", "vinho", "sabonete", "desodorante", "escova de dente", "sorvete"]

print("Lista de Compras do Mês:")
for item in compras_do_mes:
 print(item)

compras_do_mes.remove("sabonete")
compras_do_mes.remove("desodorante")
compras_do_mes.remove("escova de dente")

# Imprime a lista de compras atualizada
print("Lista de Compras do Mês:")
for item in compras_do_mes:
 print(item)