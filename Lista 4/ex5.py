texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace(":", "")
texto = texto.lower()
palavras = texto.split()
letras_alvo = "python"
contador = 0
for palavra in palavras:
    if len(palavra) > 4:
        tem_a_letra = False
        for letra in palavra:
            if letra in letras_alvo:
                tem_a_letra = True
                break 
        if tem_a_letra == True:
            contador = contador + 1

print("Total de palavras que passaram nas regras:", contador)
