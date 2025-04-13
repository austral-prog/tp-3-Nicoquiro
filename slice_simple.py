def slice_simple():
    texto = "Awesome"

    texto = texto.lower()

    primera = texto[0:3]
    las_cuatro_iniciales = texto[0:4]
    segunda = texto[2:5]
    ultima = texto[4:7]

    print(primera)
    print(segunda)
    print(las_cuatro_iniciales + ultima)
    
