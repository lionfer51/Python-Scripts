import os
archivos=os.listdir()
i=0
for archivo in archivos:
    if ".jpg" in archivo:
         os.rename(archivo,str(i)+".jpg")
         print("renombrando")
         i+=1