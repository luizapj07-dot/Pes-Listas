x = -1

while x != 0:


    def conversor_reais(valor):
        reais = int(valor // 1)
        return reais

    def conversor_centavos(valor):
        centavos = round((valor%1)*100)
        return centavos


    def extenso_reais(num1):
        especiais =  {
            0: "zero",
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
        dezenas = {
            2: "vinte",
            3: "trinta",
            4: "quarenta",
            5: "cinquenta",
            6: "sessenta",
            7: "setenta",
            8: "oitenta",
            9: "noventa"
        }
        centenas = {
            1: "cento",
            2: "duzentos",
            3: "trezentos",
            4: "quatrocentos",
            5: "quinhentos",
            6: "seiscentos",
            7: "setecentos",
            8: "oitocentos",
            9: "novecentos"
        }

        if num1 > 19:
            alt = num1 #definindo alt
            milhar = alt // 1000 #milhares
            alt = alt % 1000#atualizar alt

            centena = alt // 100 #centenas
            alt = alt%100#atualizar alt

            dezena = alt // 10 #dezenas
            alt = alt %10 #atualizar alt



        if num1 <= 19:
            return especiais[num1] + "reais e "
        else:
            if milhar > 0:
                return especiais[milhar] + " mil " + centenas[centena] + " e " + dezenas[dezena] + " e " + especiais[alt] + " reais e "
            elif centena > 0:
                return centenas[centena] + " e " + dezenas[dezena] + " e " + especiais[alt] + "reais e "
            elif dezena > 0:
                return dezenas[dezena] + " e " + especiais[alt] + " reais e "
            elif alt > 0:
                return especiais[alt] + " reais e "
            else:
                return "0 reais e "


    def extenso_centavos(num2):
        especiais2 =  {
            0: "zero",
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
        dezenas2 = {
            2: "vinte",
            3: "trinta",
            4: "quarenta",
            5: "cinquenta",
            6: "sessenta",
            7: "setenta",
            8: "oitenta",
            9: "noventa"
        }

        if num2 > 19:
            alt2 = num2
            dezena2 = alt2 // 10 #dezenas
            alt2 = alt2 %10 #atualizar alt


        if num2 <= 19:
            return especiais2[num2] + " centavos "
        else:
            if alt2 == 0:
                return dezenas2[dezena2] + " centavos"
            else:        
                return dezenas2[dezena2] + " e " + especiais2[alt2] + " centavos"


    valor = float(input("Digite uma quantia em dinheiro: "))

    print(extenso_reais(conversor_reais(valor)), extenso_centavos(conversor_centavos(valor)))
