
def Volume(a, b):
    Area = (3.14)*(a*a)*(b)
    return Area

Raio = int(input("Qual é o raio do cilindro? "))
Altura = int(input("Qual é a altura do cilindro? "))
print(Volume(Raio, Altura))