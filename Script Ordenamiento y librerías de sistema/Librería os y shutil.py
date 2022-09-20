#Uso de la librería OS
import os
#Directorio actual
os.getcwd()
#Cambio de directorio
os.chdir(r'dirección_a_mover')
#Comprobar la existencia de un directorio
os.path.exists(r'directorio_a_comprobar')
#Obtener lista de carpetas y archivos
os.listdir()
#Creación de directorios
os.makedirs('nombre_directorio')
#Eliminar directorios vacíos
os.rmdir(r'ruta_de_la_carpeta_a_eliminar')
#Eliminar carpeta con archivos
import shutil
shutil.rmtree(r'ruta_de_la_carpeta_a_eliminar')
#Renombrar archivos
os.rename('nombre_archivo.txt','nuevo_nombre.txt')
#Eliminar archivos
##Ruta actual
os.remove('nombre_archivo')
##Otras Rutas
os.remove(r'ruta_del_archivo')
#Cambiar archivos de ubicación 
import shutil
shutil.move('nombre_archivo',r'ruta_a_mover')
#Copiar archivos
import shutil
shutil.copy('nombre_archivo','ruta_a_copiar')