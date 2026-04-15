# Escreva um programa que permita que o usuário pergunte sua altura, cor favorita
# ou autor favorito e retorne o resultado a partir do dicionário criado no desa�o
# anterior.

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")
color = input("Enter your color: ")

you = {
    "name": name,
    "age": age,
    "height": height,
    "weight": weight,
    "color": color
}

print("Here is your info: ", you)