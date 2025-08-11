import random
def main():
    notas = [0.0] * 4
    media = 0
    for i in range( len ( notas)):
        notas[i] = random.uniform(0, 10)
        media += notas[i]
    
    media /= 4

    print(f"A media foi {media:,.3}")

    if media >= 6:
        print("Aprovada")
    elif media >= 4:
        print("Recuperação")
    else:
        print("Reprovado")




    return 0
main()