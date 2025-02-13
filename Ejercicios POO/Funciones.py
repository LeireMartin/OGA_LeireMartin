#Las funciones o metodos siempre e declaran con def:

def saludo():
    print("¿Hola cómo estás?")
saludo()
def suma(a,b):
    return a+b

resultado=suma(3,4)
print("La suma es: ",resultado)

def es_par(num):
    if num%2==0:
        return True;
    else:
        return False;
# return num%2==0 Hace lo mismo
print(es_par(6))

