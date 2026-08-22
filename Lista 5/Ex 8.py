x = 1
while x > 0:

    horario = str(input("Que horas são?  "))

    hora, minuto = map(int, horario.split(":"))

    def converter(hora, minuto):

        if hora == 0:
            return f"12:{minuto:02d} A.M"

        elif hora < 12:
            return f"{hora}:{minuto:02d} A.M"

        elif hora == 12:
            return f"{hora}:{minuto:02d} P.M"

        else:
            hora = hora - 12
            return f"{hora}:{minuto:02d} P.M"

    print(converter(hora, minuto))



    