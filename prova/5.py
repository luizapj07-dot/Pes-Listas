num = int(input("Digite um numero: "))

if num >= 1:
    for i in range (num):
        i += 1
        print(i)    
else:
    i = 1
    while i >= num:
        print(i) 
        i -= 1
        