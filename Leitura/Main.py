def main():
    nome = input ("Digite o  seu nome: ")
    idade = int ( input ("Digite a sua idade: "))
    altura = float ( input ("Digite a sua altura: "))
    isMasculino = input ("Vc é do sexo masculino? ")

    print("O ", nome, " tem ", idade, " anos de idade e ", altura, "metros de altura")

    if isMasculino == "Sim" or isMasculino == "s":
        print("É masculino")
    elif isMasculino == "Sou":
        print("Ele é masculino")    
    else:
        print("É feminino")


    return 0
main()