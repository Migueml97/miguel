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

#Ejercicio 2 -> Validador de IP's

IP = input("Introduce una IP: ")

test = ["192.168.1.1", "192.168.1.01", "01.02.03.04", "....", "192.a.1.1", "256.0.0.1", "192.168.1.1.1", "192.168.1"]
def validar_ip(ip) -> bool:
    octetos = ip.split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        try:    
            octeto = int(octeto)
        except ValueError:
            return False
        if octeto < 0 or octeto >255:
            return False
    return True

print(validar_ip(IP))

#tambien se puede hacer con la libreria import ipaddress
#IP = input("Introduce una IP")
#def validar_ip(ip):
#try:
#ipaddress.ip_address(ip)
#except ValueError:
#return False
#return True
#print(validar_ip(IP))

#Ejercicio 3 -> ordenar una lista (pdt) *copiado
cadena = "111 333 222"
def order_weight(strng: str) -> str:  # "111 333 222"
    secuencia = strng.split()  # Dividimos en numeros ["111", "333", "222"]
    secuencia_final = sorted(secuencia, key=ordenar)  # Ordename LISTA por PRIMERO numero total y LUEGO los digitos
    return ' '.join(secuencia_final)  # Se devuelve una lista ordenada como STRING con ESPACIOS
print(order_weight(Cadena))


            

