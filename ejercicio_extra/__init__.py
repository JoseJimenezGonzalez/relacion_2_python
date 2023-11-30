#Descripción del Problema: Escribe un programa que analice los datos de
#ventas de una tienda. El programa debe calcular y mostrar estadísticas como la
#venta total, el promedio de ventas, la venta más alta y la más baja. Los datos
#de ventas se pueden representar como una lista de números, donde cada
#número representa el total de ventas de un día.
#Requerimientos Específicos:
#1. Representación de los Datos de Ventas: Usa una lista para
#representar los datos de ventas. Puedes inicializar la lista con datos
#estáticos o permitir al usuario ingresar los datos.
#2. Función para Calcular la Venta Total: Crea una función que sume
#todos los valores en la lista de ventas para obtener la venta total.
#3. Función para Calcular el Promedio de Ventas: Implementa una
#función que calcule el promedio de ventas. Esta función debe sumar
#todas las ventas y dividirlas por el número de días.
#4. Función para Encontrar la Venta Más Alta y Baja: Escribe una función
#que encuentre y devuelva la venta más alta y la más baja en la lista.
#5. Presentación de Resultados: Después de realizar los cálculos, el
#programa debe imprimir los resultados: total de ventas, promedio de
#ventas, venta más alta y venta más baja.
#6. Validación de Datos: Asegúrate de que las funciones manejen
#adecuadamente listas vacías o datos no válidos.
dias_tiendaAbierta = ["lunes", "martes", "miercoles", "jueves", "viernes"]
ventas_por_dia = [10, 12, 8, 6, 5]
venta_lunes = [3.59, 9.65, 12, 10, 8, 78, 78, 85, 96, 105.63]
venta_martes = [8, 9.65, 12, 10, 8, 78, 95, 85, 96, 105.63, 5, 87]
venta_miercoles = [8, 9.65, 12, 10, 8, 78, 78, 85]
venta_jueves = [8, 9.65, 12, 10, 8, 78]
venta_viernes = [78, 9.65, 12, 10, 400]

ventas_dias = [venta_lunes, venta_martes, venta_miercoles, venta_jueves, venta_viernes]

def ventaTotal():
    suma_total = 0
    for dias in ventas_dias:
        for valor_de_cada_venta in dias:
            suma_total += valor_de_cada_venta
    return suma_total

def ventaTotalPorDia(dia_semana):
    suma_total = 0
    posicion_dia = dias_tiendaAbierta.index(dia_semana)
    for venta in ventas_dias[posicion_dia]:
        suma_total += venta
    return suma_total

def promedioVentas():
    sumatoria = 0
    for ventas_dia in ventas_por_dia:
        sumatoria += ventas_dia
    return sumatoria / len(ventas_por_dia)

def ventaMasCara():
    mayor = ventas_dias[0][0]
    for dias in ventas_dias:
        for venta in dias:
            if(venta > mayor):
                mayor = venta
    return mayor


def ventaMasBarata():
    menor = ventas_dias[0][0]
    for dias in ventas_dias:
        for venta in dias:
            if(venta < menor):
                menor = venta
    return menor


venta_total = ventaTotal()
dia_elegido_venta = "viernes"
venta_dia_elegido = ventaTotalPorDia(dia_elegido_venta)
promedio_de_ventas = promedioVentas()
venta_mas_cara = ventaMasCara()
venta_mas_barata = ventaMasBarata()
print(f"El importe de las ventas totales asciende a {venta_total} euros")
print(f"El dia {dia_elegido_venta} se ha vendido productos por valor de {venta_dia_elegido}")
print(f"Promedio ventas: {promedio_de_ventas}")
print(f"Venta mas cara: {venta_mas_cara} euros")
print(f"Venta mas barata: {venta_mas_barata} euros")
