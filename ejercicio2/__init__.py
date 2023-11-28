# Conversor de Temperatura:
# Haz un programa que convierta temperaturas de Celsius a Fahrenheit y
# viceversa. El usuario debe poder elegir qué conversión realizar.

def celsiusToFahrenheit(temperatura_en_celsius):
    return (temperatura_en_celsius * 9 / 5) + 32


def fahrenheitToCelsius(temperatura_en_fahrenheit):
    return (temperatura_en_fahrenheit - 32) * 5 / 9


print("Conversor de temperatura, introducir número por teclado según elección:")
print("1. Conversor de celsius a fahrenheit")
print("2. Conversor de fahrenheit a celsisus")
eleccion = int(input())
print("Introduzca temperatura a convertir")
temperatura_usuario = float(input())
mensaje = ""
if(eleccion == 1):
    resultado = celsiusToFahrenheit(temperatura_usuario)
    mensaje = f"{temperatura_usuario}ºC equivalen a {resultado}ºF."
elif(eleccion == 2):
    resultado = fahrenheitToCelsius(temperatura_usuario)
    mensaje = f"{temperatura_usuario}ºF equivalen a {resultado}ºC."
else:
    mensaje = "Esa opción no existe."

print(mensaje)
