from pytube import YouTube
c_v=set()
c_a=set()
enlace=input('Escribe o pega el enlace del video:\n')
vid=YouTube(enlace)
opt=int(input('Quieres descargar?\n1-Video\n2-Audio\nElige una opción: '))
print("Analizando...")
v_lib=vid.streams.filter(progressive=True)
for i in v_lib:
    if i.type=='video':
        c_v.add(int(i.resolution[:-1]))
    else:
        c_a.add(int(i.abr[:-4]))
l_cv=sorted(list(c_v))
l_ca=sorted(list(c_a))

if opt==1:
    for i in l_cv:
        print(str(l_cv.index(i)+1)+"- "+str(i)+"p")
    opt_c=input("Elige la calidad que quieres descargar: 1-"+str(len(l_cv))+" \n")
    v_d=v_lib.filter(type='video').filter(res=str(l_cv[int(opt_c)-1])+"p")[0]
    print("Empezando a descargar...")
    print(v_d.title+" a "+ "\""+v_d.resolution+"\"")
    print("Tamaño aprox: "+str(round(v_d.filesize/1e6,2))+" MB")
    v_d.download()
else:
    for i in l_ca:
        print(str(l_ca.index(i)+1)+"- "+str(i)+" Kbps")
    opt_c=input("Elige la calidad que quieres descargar: 1-"+str(len(l_ca))+" \n")
    a_d=v_lib.filter(type='audio').filter(abr=str(l_ca[int(opt_c)-1])+"kbps")[0]
    print(a_d.title+" a "+ "\""+a_d.abr+ "\"")
    print("Empezando a descargar...")
    print("Tamaño aprox: "+str(round(a_d.filesize/1e6,2))+" MB")
    a_d.download()
print("Descarga Finalizada c:")