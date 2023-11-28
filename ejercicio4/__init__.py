#Contador de Vocales y Consonantes:
#Haz un programa que cuente el número de vocales y consonantes en una
#cadena de texto proporcionada por el usuario.
def contadorVocales(texto):
    return sum(map(texto.lower().count, "aeiouáéíóúü"))

def contadorConsonantes(texto):
    return sum(map(texto.lower().count, "qwrtypsdfghjklñzxcvbnm"))

print("Introduce una cadena de texto para contar vocales y consonantes")
texto = input()
numero_de_vocales = contadorVocales(texto)
numero_de_consonantes = contadorConsonantes(texto)
mensaje = f"En el texto hay {numero_de_vocales} vocal/es y {numero_de_consonantes} consonante/s"
print(mensaje)