#Receber a quantidade de notas pelo usuário que será calculado e no final calcular a média final
quantidade = int(input("Digite a quantidade de notas que serão calculadas: "))
notas = []
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
media = sum(notas) / quantidade
print(f"A média das suas notas é: {media:.2f}")
