import os
from google_images_download import google_images_download   #importing the library
response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords":"","limit":0,"print_urls":True}   #creating list of arguments
c_busquedas=int(input("Escribe la cantidad de búsquedas que harás: "))
c_img=int(input("Escribe la cantidad de imágenes a descargar por búsqueda 0-100: "))
arguments['limit']=c_img
print("Escribe las búsquedas que deseas realizar, recuerda no utilizar carácteres especiales")
i=0
while i<c_busquedas:
    keyword=input(str(i+1)+": " )
    print(i)
    if i==0:
        arguments['keywords']+=keyword
    else:
        arguments['keywords']+=","+keyword
    i+=1
    print(arguments['keywords'])
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
os.system('clear')
print("Tus archivos se han descargado, revisa la carpeta Downloads")