def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_entre_1_e_50():
    for num in range(1, 51):
        if eh_primo(num):
            print(num)

imprimir_primos_entre_1_e_50()