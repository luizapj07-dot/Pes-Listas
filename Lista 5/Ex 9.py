Data = str(input("Ponha uma data: "))

dia, mes, ano = map(int, Data.split("/"))

def extenso_dia(num):
    especiais = {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
        20: "vinte",
        21: "vinte e um",
        22: "vinte e dois",
        23: "vinte e três",
        24: "vinte e quatro",
        25: "vinte e cinco",
        26: "vinte e seis",
        27: "vinte e sete",
        28: "vinte e oito",
        29: "vinte e nove",
        30: "trinta",
        31: "trinta e um"
    }
    dia_extenso = especiais[num]
    return dia_extenso

def extenso_mes(num2):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    mes_extenso = meses[num2]
    return mes_extenso

def extenso_ano(num3):
    especiais2 =  {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
        }
    grandes = {
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "setenta",
        80: "oitenta",
        90: "noventa"
    }

    ano_mes = ((num3%100)//10)*10
    ano_dia= num3%10

    if num3 % 100 <= 19:
        ano_extenso = "dois mil e " + especiais2[num3 % 100]
    elif ano_dia == 0:
        ano_extenso = "dois mil e " + grandes[ano_mes]
    else:
        ano_extenso = "dois mil e " + grandes[ano_mes] + " e " + especiais2[ano_dia]

    return ano_extenso

print(f"A data é {extenso_dia(dia)} de {extenso_mes(mes)} de {extenso_ano(ano)}")