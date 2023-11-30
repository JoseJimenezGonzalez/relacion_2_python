#Crea una función que convierta segundos en horas, minutos y segundos. La
#función debe tomar un número entero que represente los segundos y devolver
#una cadena en el formato "HH:MM:SS".

segundos_a_convertir = 59


def segundosAFormatoTexto(segundos):
   horas = int(segundos / 3600)
   resto_horas = int(segundos % 3600)
   minutos = int(resto_horas / 60)
   resto_minutos = int(resto_horas % 60)
   return str(horas) + ":" + str(minutos) + ":" + str(resto_minutos)


print(f"{segundos_a_convertir} segundos equivale a -> {segundosAFormatoTexto(segundos_a_convertir)}")


