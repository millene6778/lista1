def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero_digitado = int(input("Digite um número: "))
resultado = verificar_par_impar(numero_digitado)
print(f"O número {numero_digitado} é {resultado}.")