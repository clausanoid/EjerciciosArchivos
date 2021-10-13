""" Importamos la libreria csv para poder manipular archivos csv"""
import csv

""" Funcion que permite crear un archivo .csv con el nombre Nomina"""
def crear_archivo():
    """ Creamos una variable con el nombre archivo nomina que sera donde guardaremos y crearemos el archivo .csv"""
    archivo_nomina = open('Nomina.csv', 'a+')
    """ Devolvemos un archivo tipo .csv llamado Nomina"""
    return archivo_nomina

""" Funcion que nos permite agregar datos al archivo Nomina.csv, solicitando el numero de empleados a ingresar """
def agregar_datos(cantidad_usuarios):
    """Por cada empleado que queramos ingresar, vamos a crear un arreglo, solicitar y calcular los datos y escribirlos en el archivo Nomina.csv"""
    for empleado in range(cantidad_usuarios):
        datos = []
        nombre = input("Ingrese nombre del empleado: ")
        numero_empleado = input("Ingrese numero de empleado: ")
        nivel = input(
            "Ingrese el nivel del empleado utilizando solo una letra para cada nivel, manual (m), cualificado (c), oficinista (o), directivo (d): ")
        if nivel == "o" or nivel == "d":
            complemento = 15
        else:
            complemento = 0
        sueldo = input("Ingrese sueldo del empleado: ")
        sueldo_bruto = int(sueldo) + complemento
        excencion = input("Ingrese monto a excentar: ")
        impuesto = (sueldo_bruto - int(excencion)) * 0.33
        datos.append(nombre)
        datos.append(numero_empleado)
        datos.append(nivel)
        datos.append(complemento)
        datos.append(sueldo)
        datos.append(sueldo_bruto)
        datos.append(excencion)
        datos.append(impuesto)
        with open('Nomina.csv', 'a') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(datos)
    return 'Datos agregados correctamente'

""" Funcion que permite modificar los datos de un usuario en base a su nombre de usuario """
def modificar_datos(id):
    """Creamos un arreglo donde guardaremos los datos modificados"""
    nuevos_datos = []
    """Definimos los nombres de los campos de nuestro csv para poderlos comparar y modificar"""
    nombres_de_campos = ["Nombre", "Numero Empleado", "Nivel Empleado", "Complemento", "Sueldo", "Sueldo Bruto",
                         "Excencion", "Impuesto"]
    """Abrimos el archivo Nomina.csv"""
    with open('Nomina.csv', 'r') as archivo:
        """ Creamos una variable lector para leer los contenidos del archivo Nomina.csv"""
        lector = csv.DictReader(archivo, fieldnames=nombres_de_campos)
        """Sacamos los valores de cada columna y si una contiene el numero de empleado que ingresamos nos solicita los valores nuevos"""
        for columna in lector:
            if id == columna['Numero Empleado']:
                columna["Nombre"] = input("Ingrese nuevo nombre: ")
                columna["Numero Empleado"] = input("Ingrese nuevo numero de empleado: ")
                columna["Nivel Empleado"] = input(
                    "Ingrese el nivel del empleado utilizando solo una letra para cada nivel, manual (m), cualificado (c), oficinista (o), directivo (d): ")
                if columna["Nivel Empleado"] == "o" or columna["Nivel Empleado"] == "d":
                    columna["Complemento"] = 15
                else:
                    columna["Complemento"] = 0
                columna["Sueldo"] = input("Ingrese nuevo sueldo:")
                columna["Sueldo bruto"] = int(columna["Sueldo"]) + int(columna["Complemento"])
                columna["Excencion"] = input("Insertar monto a excentar: ")
                columna["Impuesto"] = int(columna["Sueldo Bruto"]) - int(columna["Excencion"]) * 0.33
                nuevos_datos.append(
                    {'Nombre': columna['Nombre'], 'Numero Empleado': columna['Numero Empleado'],
                     'Nivel Empleado': columna['Nivel Empleado'], 'Complemento': columna['Complemento']
                        , 'Sueldo': columna['Sueldo'], 'Sueldo Bruto': columna['Sueldo Bruto'],
                     'Excencion': columna['Excencion']
                        , 'Impuesto': columna['Impuesto']})
            else:
                nuevos_datos.append(
                    {'Nombre': columna['Nombre'], 'Numero Empleado': columna['Numero Empleado'],
                     'Nivel Empleado': columna['Nivel Empleado'], 'Complemento': columna['Complemento']
                        , 'Sueldo': columna['Sueldo'], 'Sueldo Bruto': columna['Sueldo Bruto'],
                     'Excencion': columna['Excencion']
                        , 'Impuesto': columna['Impuesto']})
        """Escribimos los valores nuevos en un archivo temporal y luego los modificamos en el archivo original"""
        with open('Nomina.csv', 'w') as salida:
            escribir = csv.DictWriter(salida, fieldnames=nombres_de_campos)
            escribir.writerows(nuevos_datos)

    return "Datos modificados correctamente"

"""Funcion que nos permite añadir una columna "Semana de antiguedad al archivo Nomina.csv"""
def añadir_semana():
    nuevos_datos = []
    nombres_de_campos = ["Nombre", "Numero Empleado", "Nivel Empleado", "Complemento", "Sueldo", "Sueldo Bruto",
                         "Excencion", "Impuesto", "Semanas Antiguedad"]
    with open('Nomina.csv', 'r') as archivo:
        lector = csv.DictReader(archivo, fieldnames=nombres_de_campos)
        for columna in lector:
            nuevos_datos.append(
                {'Nombre': columna['Nombre'], 'Numero Empleado': columna['Numero Empleado'],
                 'Nivel Empleado': columna['Nivel Empleado'], 'Complemento': columna['Complemento']
                    , 'Sueldo': columna['Sueldo'], 'Sueldo Bruto': columna['Sueldo Bruto'],
                 'Excencion': columna['Excencion']
                    , 'Impuesto': columna['Impuesto'], "Semanas Antiguedad": "1"})

        with open('Nomina.csv', 'w') as salida:
            escribir = csv.DictWriter(salida, fieldnames=nombres_de_campos)
            escribir.writerows(nuevos_datos)

    return "Agregado correctamente"

"""Funcion que lee los valores de Nomina.csv y los imprime en pantalla """
def mostrar_listado():
    print(
        "Nombre " + " Nivel " + "Sueldo " + "Complemento " + "Sueldo Bruto " + "Excencion " + "Impuesto " + "Sueldo neto")
    nombres_de_campos = ["Nombre", "Numero Empleado", "Nivel Empleado", "Complemento", "Sueldo", "Sueldo Bruto",
                         "Excencion", "Impuesto", "Semanas Antiguedad"]
    with open('Nomina.csv', 'r') as archivo:
        lector = csv.DictReader(archivo, fieldnames=nombres_de_campos)
        for columna in lector:
            sueldoNeto = (float(columna["Sueldo Bruto"]) - float(columna["Excencion"])) - float(columna["Impuesto"])
            print(columna["Nombre"] + " " + columna["Nivel Empleado"] + " " + columna["Sueldo"] + " " + columna[
                "Complemento"] + " " + columna["Sueldo Bruto"]
                  + " " + columna["Excencion"] + " " + columna["Impuesto"] + " " + str(sueldoNeto))


def main():
    print("Seleccione una opción del menu:")
    print("1.Cree el fichero vacío")
    print("2.Añada registros")
    print("3.Modifique los valores de un registro por el número de empleado")
    print("4.Añada una semana de antigüedad a todos los empleados.")
    print("5.Mostrar listado")
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        crear_archivo()
    elif opcion == "2":
        numero = int(input("Ingrese numero de empleados a capturar: "))
        agregar_datos(numero)
    elif opcion == "3":
        numero = input("Ingrese numero de empleado a editar: ")
        modificar_datos(numero)
    elif opcion == "4":
        añadir_semana()
    elif opcion == "5":
        mostrar_listado()


if __name__ == "__main__":
    main()
