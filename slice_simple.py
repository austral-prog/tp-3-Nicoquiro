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
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
