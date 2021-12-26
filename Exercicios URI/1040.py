n1, n2, n3, n4 = input().split(" ")

total_ponderado = (2*float(n1)) + (3*float(n2)) + (4*float(n3)) +(1*float(n4))
total_pesos = 2 + 3 + 4 + 1

media = total_ponderado / total_pesos

if media >= 7.0:
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
elif media < 5.0:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9:
    exame = float(input())

    nova_media = ((media + exame) / 2)
    if media >= 5.0:
        analise = "Aluno aprovado."
    elif media < 4.9:
        analise = "Aluno reprovado."

    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")
    print("Nota do exame: {:.1f}".format(exame))
    print(analise)
    print("Media final: {:.1f}".format(nova_media))
    