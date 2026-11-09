from src.funciones import nombre
from src.clases import Tarea, Gestor
a = True
gestor = Gestor()

print("***BIENVENIDO AL PROGRAMA***")

while a:
    try:
        accion = int(input("""***Este es el menu***
            (1) Añadir tarea
            (2) Borrar tarea
            (3) Mostrar tareas
            (4) Completar tarea
            (5) Salir del programa
                
    Accion : """))

        if accion == 1:
            nombre_tarea = nombre()
            tarea = Tarea(nombre_tarea, completada="Pendiente")
            gestor.añadir_tarea(tarea)
        elif accion == 2:
            nombre_tarea = nombre()
            gestor.borrar_tarea(nombre_tarea)
        elif accion == 3:
            gestor.mostrar_tareas()
        elif accion == 4:
            nombre_tarea =nombre()
            gestor.completar_tarea(nombre_tarea)
        elif accion ==5:
            a = False
        else:
            pass
    except ValueError:
        print("Elige entre (1-4)")