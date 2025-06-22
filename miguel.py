#Ejercicio 1 -> Ascensor
piso = int(input("Estás en un ascensor en la planta cero y tiene las siguentes plantas: " \
" 0 -> Hall" \
" 1 -> Comedor" \
" 2 -> Gimnasio" \
" 3 -> Biblioteca" \
" 4 -> SPA" \
" 5 -> Azotea"
" 6 -> Salir: "))

piso_actual = 0

while piso != 6:
    if piso >= 0 and piso <=5:
        if piso > piso_actual:
            print("Subiendo..")
            for planta in range(piso_actual, piso + 1):
               print(f"Ascensor en la planta {planta}")   
        elif piso < piso_actual:
            print("Bajando...")
            for planta in range(piso_actual, piso - 1, -1):
                print(f"Ascensor en la planta {planta}")
        else:
            print("Ya estas en la planta solicitada")
        print(f"Has llegado a la planta {piso}")
        piso_actual = piso
    else:
        piso = print("Introduce un número del 1 al 6: ")
    piso = int(input("Introduce un número del 1 al 6: "))
print("Adios")


            

