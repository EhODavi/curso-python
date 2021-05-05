numeros_por_extenso = ""

lista = ["", "um", "dois", "tres", "quatro", "cinco", "seis",
         "sete", "oito", "nove", "dez", "onze", "doze", "treze",
         "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

lista_dezena = ["", "", "vinte", "trinta", "quarenta", "cinquenta",
                "sessenta", "setenta", "oitenta", "noventa"]

lista_centena = ["", "cento", "duzentos", "trezentos", "quatrocentos",
                 "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

for i in range(1, 1001):
    i_string = str(i)

    if len(i_string) == 1:
        numeros_por_extenso = numeros_por_extenso + lista[i]
    elif len(i_string) == 2:
        if i < 20:
            numeros_por_extenso = numeros_por_extenso + lista[i]
        else:
            numeros_por_extenso = numeros_por_extenso + lista_dezena[int(i_string[0])]

            if i_string[1] != '0':
                numeros_por_extenso = numeros_por_extenso + "e" + lista[int(i_string[1])]
    elif len(i_string) == 3:
        if i_string == "100":
            numeros_por_extenso = numeros_por_extenso + "cem"
        else:
            numeros_por_extenso = numeros_por_extenso + lista_centena[int(i_string[0])]

            if i_string[1] != '0' or i_string[2] != '0':
                if 10 * int(i_string[1]) + int(i_string[2]) < 20:
                    numeros_por_extenso = numeros_por_extenso + "e" + lista[10 * int(i_string[1]) + int(i_string[2])]
                else:
                    numeros_por_extenso = numeros_por_extenso + "e" + lista_dezena[int(i_string[1])]

                    if i_string[2] != '0':
                        numeros_por_extenso = numeros_por_extenso + "e" + lista[int(i_string[2])]
    else:
        numeros_por_extenso = numeros_por_extenso + "mil"

print(f'Quantidade de letras: {len(numeros_por_extenso)}')
