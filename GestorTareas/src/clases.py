import json
from pathlib import Path

carpeta_src = Path(__file__).parent
localizacion_json = (carpeta_src / ".."/ "almacenamiento" / "archivo.json").resolve()

with open(localizacion_json, "r", encoding="utf-8") as archivo:
    lista_tareas = json.load(archivo)


class Gestor:
    def __init__(self):
        self.lista_tareas = lista_tareas
    
    def añadir_tarea(self, tarea):
        encontrada = False
        tarea = {
                    "nombre" : tarea.nombre,
                    "completada" : tarea.completada
                }
        for tareas in self.lista_tareas:
            if tareas['nombre'] == tarea['nombre']:
                encontrada = True
                break
        
        if encontrada == True:
            print("La tarea ya existe")
        else:
            self.lista_tareas.append(tarea)
            with open(localizacion_json, "w", encoding="utf-8") as archivo:
                json.dump(self.lista_tareas, archivo, indent=4)
    
    def mostrar_tareas(self):
        for tarea in self.lista_tareas:
            print (f"""
                    NOMBRE : {tarea['nombre']}
                    ESTADO : {tarea['completada']}
                    \n
                    """)
    
    def completar_tarea(self, nombre_tarea):
        tarea_encontrada = False
        for tarea in self.lista_tareas:
            if nombre_tarea == tarea['nombre']:
                tarea_encontrada = True
                break
            else:
                tarea_encontrada = False
        
        if tarea_encontrada == True:
            tarea['completada'] = "Completada"
            print(f"Se ha marcado como completada la tarea {tarea['nombre']}")
            with open(localizacion_json, "w", encoding="utf-8") as archivo:
                json.dump(self.lista_tareas, archivo,  indent=4)
        else:
            print(f"La tarea {nombre_tarea} no ha sido encontrada en la base de datos")
        
    def borrar_tarea(self, nombre_tarea):
        encontrada = False
        for tarea in self.lista_tareas:
            if nombre_tarea == tarea['nombre']:
                encontrada = True 
                break
            
        if encontrada == True:
            self.lista_tareas.remove(tarea)
            with open(localizacion_json, "w", encoding="utf-8") as archivo:
                json.dump(self.lista_tareas, archivo, indent=4)
        else:
            print(f"La tarea {nombre_tarea} no ha sido encontrada")
    
    def cambiar_nombre(self, nombre_tarea):
        encontrada = False
        for tarea in self.lista_tareas:
            if nombre_tarea == tarea['nombre']:
                encontrada = True
                break
        
        if encontrada == True:
            new_name = input("Cual es el nuevo nombre de su tarea: ")
            tarea['nombre'] = new_name
            with open(localizacion_json, "w", encoding="utf-8") as archivo:
                json.dump(self.lista_tareas, archivo, indent=4)
        else:
            print(f'La tarea "{nombre_tarea}" no ha sido encontrada')
    
class Tarea:
    def __init__(self, nombre, completada):
        self.nombre = nombre
        self.completada = completada