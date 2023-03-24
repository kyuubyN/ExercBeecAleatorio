a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = 0
m =0
t = [a, b, c, d, e, f]
for j in t:
    if j > 0:
        x += 1
        m = m + (j)
print(f'{x} valores positivos')
print(f"{m/x:.1f}")
#Esse codigo recebe numeros positivos e negativos e diz quantos numeros são positivos e a media dos numeros positivos
