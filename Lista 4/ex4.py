texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace(":", "")
texto = texto.lower() 
palavras = texto.split()
lista_final = []
letras_alvo = "python"
for palavra in palavras:
    primeira_letra = palavra[0]
    ultima_letra = palavra[-1]
        if primeira_letra in letras_alvo or ultima_letra in letras_alvo:
        lista_final.append(palavra)

print("As palavras aprovadas foram:")
print(lista_final)
