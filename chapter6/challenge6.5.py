# Pegue a lista ["The", "fox", "jumped", "over", "the", "fence", "."] e
# transforme-a em uma string gramaticalmente correta. É preciso que haja um
# espaço entre cada palavra, mas nenhum espaço entre a palavra fence e o ponto
# que vem depois dela. (Não se esqueça de que você conheceu um método que
# transforma uma lista de strings em uma única string).

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
phrase = " ".join(words)

print(phrase[:-2] + ".")
