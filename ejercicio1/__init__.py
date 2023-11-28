# Escribe un programa que realice operaciones básicas (suma, resta,
# multiplicación, división) entre dos números. El usuario debe elegir la operación
# a través de condicionales

# Funciones
def suma(numero1, numero2):
    return numero1 + numero2


def resta(numero1, numero2):
    return numero1 - numero2


def producto(numero1, numero2):
    return numero1 * numero2


def division(numero1, numero2):
    if (numero2 != 0):
        return numero1 / numero2


print("Selecciona una opcion, introduce número por teclado:")
print("1.Suma")
print("2.Resta")
print("3.Producto")
print("4.División")
eleccion = int(input())
print("Introduce 2 numeros por teclado para poder hacer dicha operacion")
numero1 = int(input())
numero2 = int(input())
mensaje = ""
if (eleccion == 1):
    resultado = suma(numero1, numero2)
    mensaje = f"El resultado de: {numero1} + {numero2} = {resultado}"
elif (eleccion == 2):
    resultado = resta(numero1, numero2)
    mensaje = f"El resultado de: {numero1} - {numero2} = {resultado}"
elif (eleccion == 3):
    resultado = producto(numero1, numero2)
    mensaje = f"El resultado de: {numero1} * {numero2} = {resultado}"
elif (eleccion == 4 and numero2 != 0):
    resultado = division(numero1, numero2)
    mensaje = f"El resultado de: {numero1} / {numero2} = {resultado}"
elif (eleccion == 4 and numero2 == 0):
    mensaje = "No se puede dividir entre 0, es una indeterminacion"
else:
    mensaje = "No existe esa opcion"

print(mensaje)
