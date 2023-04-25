nota1 = float(input("Nota p1: "))
nota2 = float(input("Nota p2: "))
nota3 = float(input("Nota p3: "))

media = nota1 + nota2 + (nota3 / 3)

print(f"{media}")

if media >= 6:
    print("Parabéns você foi aprovado !")
elif media < 6:
    print("você foi reprovado")
