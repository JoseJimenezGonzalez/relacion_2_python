#Función para Convertir Números a Formato Romano:
#Desarrolla una función que tome un número entero y lo convierta en su
#equivalente en números romanos. Por ejemplo, el número 5 se convierte en "V"
#y el 12 en "XII"
diccionario = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanoADecimal(numero_romano):
    sum = 0
    for num_romano in numero_romano:
        sum += diccionario.get(num_romano)
    return sum


numero_romano_a_convertir = "XVI"
resultado =  romanoADecimal(numero_romano_a_convertir)
print(f"El numero romano {numero_romano_a_convertir} equivale a {resultado} en decimal.")