notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(4)]
media = sum(notas) / 4
print(f"Sua média é: {media:.2f}\n{'Aprovado!' if media >= 7 else 'Reprovado.'}")
