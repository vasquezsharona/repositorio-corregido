#play={'Artistas':{'genero':{'canciones':'duracion'}}}
def nuevoArtista(play1,art,genero,can,dur):
    play1.update({art:{genero:{can:dur}}})

playlist={}

while True:
    x=int(input('\nPresione 1 para ingresar artista\nPresione 2 para buscar cancion\nPresione 0 para salir' ))

    if x == 1:
        art=input('Ingrese artista: ')
        genero=input('Ingrese genero:')
        can=input('Ingrese cancion: ')
        dur=int(input('Ingrese duracion: '))
        nuevoArtista(playlist,art,genero,can,dur)
        print(playlist)
        while True:
            x2=int(input('Ingrese 1 para agregar canciones\n Ingrese 0 para salir '))
            if x2 == 1:
                can=input('Ingrese cancion: ')
                dur=int(input('Ingrese duracion: '))
                #playlist.update({art:{genero:{can:dur}}})
                playlist[art][genero][can]=dur
            else:
                break
    elif x==2:
        art2=input('Ingrese cancion a buscar')
        if art2 in playlist[art][genero]:
            print('si esta')
        else:
            print('No')
    else:
        print('Saliste')
        break

keys=list(playlist.keys())
print(keys[0][1])
