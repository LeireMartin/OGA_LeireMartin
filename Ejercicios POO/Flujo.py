if True:
    print("Hola")
    print("otra linea")
#print("hola") Aqui no llega la condicion
a=5
if a==2:
    print("a Vale 2")
if a==5:
    print("a vale 5")
#ANIDACIÓN-- NO ENTRA EN LAS DOS CONDICIONES SOLO EN LA PRIMER
if a==2:
    print("a vale 2")
    if a==5:
        print("a vale 5")

n=11
if n%2==0:
    print("El numero es par")
else:
    print("El numero es impar")
comando="Otra cosa"
if comando=="Entrar":
    print("bienvenido")
elif comando=="Salida":
    print("Adios")
else:
    print("No se reconoce")

#------Introduccion de datos----
nota=float(input("Introduce nota: "))
if nota<5:
    print("Insuficiente")
elif nota==5:
    print("Suficiente")
elif nota==6:
    print("Bien")
elif nota>6 and nota<9:
    print("Notable")
elif nota>8:
    print("Sobresaliente")
#-----Bucles----
c= 0
while c<=6:
    c+=1
    print("c vale:",c)

for i in range(1,11):
    print(f"Tabla del {i}:",i)
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
num= int(input("Introduce numero del 1 al 10 : "))

print(f"Tabla de {num}")

for i in range(1,11):
    print(f"{num}x{i} = {num*i}")

