# Escreva um programa que colete duas strings com um usuário, insira-as na string
# "Yesterday I wrote a [resposta_um]. I sent it to [resposta_dois]!" e
# exiba uma nova string.

str1 = input("Enter a first string: ")
str2 = input("Enter a second string: ")

phrase1 = "Yesterday I wrote a {}. I sent it to {}! ".format(str1, str2)

print(phrase1)
