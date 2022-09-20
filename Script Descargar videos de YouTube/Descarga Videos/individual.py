from pytube import YouTube
import msvcrt
enlace="https://www.youtube.com/watch?v=LXb3EKWsInQ&t=108s&ab_channel=Jacob%2BKatieSchwarz"

yt=YouTube(enlace)

lista_formatos=yt.streams.filter(progressive=False)

for x in range(0,len(lista_formatos)):
    print("---Elemento "+str(x+1)+"---")
    print("Itag: "+str(lista_formatos[x].itag))
    print("Tipo: "+lista_formatos[x].type)
    if lista_formatos[x].type=="video":
        print("Resolución: "+str(lista_formatos[x].resolution))
        print("Título: "+lista_formatos[x].title)
        print("Tipo: "+lista_formatos[x].type)
        #print("Resolución: "+lista_formatos[x].resolution)
        print("Tamaño aprox: "+str(round(lista_formatos[x].filesize/1e6,2))+" MB")
        print("Formato: "+lista_formatos[x].mime_type)
    else:
        print("Calidad: "+lista_formatos[x].abr)
        print("Título: "+lista_formatos[x].title)
        print("Tipo: "+lista_formatos[x].type)
        #print("Resolución: "+lista_formatos[x].resolution)
        print("Tamaño aprox: "+str(round(lista_formatos[x].filesize/1e6,2))+" MB")
        print("Formato: "+lista_formatos[x].mime_type)
        
seleccion=str(input('Ingresa el itag a descargar: '))
video=yt.streams.get_by_itag(seleccion)
video.download("D:/")