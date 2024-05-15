numeros = []
for _ in range(7):
  numero = int(input('Ingrese numero: '))
  numeros.append(numero)
print(f"{numeros}")

seEncontro = False

for n in numeros:
  if n > 0 :
    seEncontro = True

if seEncontro:
    print('Hay algun numero positivo')
else:
    print('No hay positivo')