#Escribe un programa que lea un archivo de texto y que lo escriba en otro realizando los siguientes cambios:
#si es una letra minúscula la letra la guarde en mayúsculas.
#Si es numero lo ponga en código ASCII, pero con el prefijo ASC; el ejemplo se lee 9 se escribiría ASC57.
#En el caso de ser números compuestos como 57 se realizará una combinación para que genere una letra. Ejemplo #D2R2B
#En caso de caracteres especiales se dejarán iguales.
#Con excepción de # que se pondrá \# por el uso especial con los números.
"""Creamos una lista para guardar las lineas del archivo"""
lineas = []
""" Creamos el archivo nuevo donde se guardaran los valores transformados """
archivo2 = open('texto2.txt', "w+")
""" Leemos el archivo original """
with open('datos.txt') as archivo:
    lineas = archivo.read().splitlines()

""" Para cada linea en el archivo original, leemos el valor de la linea y escribimos el valor transformado en el nuevo archivo """
for linea in lineas:
    if linea.islower() == True:
        archivo2.write(linea.upper() +"\r\n")
    elif linea.isnumeric() == True and len(linea) <= 1:
        archivo2.write("ASC"+ str(ord(linea)) +"\r\n")
    elif linea.isnumeric() == True and len(linea) > 1:
        archivo2.write("#D2R2B"+"\r\n")
    elif linea == "#":
        archivo2.write("\#"+"\r\n")
    elif linea.islower() != True and linea.isnumeric() != True and linea != "#":
        archivo2.write(linea +"\r\n")


    """ Cerramos los archivos abiertos"""
    archivo.close()

