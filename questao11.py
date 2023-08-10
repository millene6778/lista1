def sao_par_inverso(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
resultado = sao_par_inverso(palavra1, palavra2)

if resultado:
    print("As palavras são um 'par inverso'.")
else:
    print("As palavras não são um 'par inverso'.")