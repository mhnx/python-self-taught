# Escreva um programa com um loop infinito (com a opção de digitar q para sair) e
# uma lista de números. A cada iteração do loop, peça ao usuário para fornecer um
# número da lista e informe se o seu palpite estava ou não correto.

numbers = [1, 2, 3, 5, 7, 9]

while True:
    ans = input("Enter a number to find out if it exists in the list. Press 'q' to quit. ")
    if ans == "q":
        print("Goodbye!")
        break

    ans = int(ans)
    if ans in numbers:
        print("{} is in the list!".format(ans))
    else:
        print("{} is not in the list!".format(ans))
