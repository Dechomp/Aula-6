def main():
    num = int ( input ("Digite um número: "))

    i = 2

    while num != 1:
        if num % i == 0:
            break
        i += 1

    if num == i:
        print("O numero", num, " é primo")
    elif num == 1:
        print("O número 1 não é primo")
    else:
        print("O número", num, "não é primo porque é divisivel por", i)

    return 0
main()