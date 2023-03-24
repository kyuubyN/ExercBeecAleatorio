a = 0
al = gs = di = 0
while a != 4:
    a = int(input())
    while a < 1 and a > 4:
        a = int(input())
    if a == 1:
        al += 1
    elif a == 2:
        gs += 1
    elif a == 3:
        di += 1
print(f"MUITO OBRIGADO\nAlcool: {al}\nGasolina: {gs}\nDiesel: {di}")
#Enquanto o numero não for == 4, o codigo vai adicionar quantidade de itens pelo numero selecionado seja ele 1 2 ou 3
