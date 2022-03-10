#Este es el código de la búsqueda de Andrés Serrano Rodríguez, sirve para realizar búsquedas en la agenda a partir de nombres de usuarios.
def buscar_ASerrano(nombre, agenda):
        for cadena,numero in agenda.items():
                if cadena.startswith(nombre):
                        print("El número de teléfono de %s es el %s " % (nombre,agenda[cadena]))   




