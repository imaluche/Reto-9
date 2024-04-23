
#Se usara una funcion que busca evaluar si un caracter es un digito o no segun el codigo ASCII, es el tercer punto del reto 4
if __name__=="__main__":
    cadena:str=str(input("cadena a evaluar:"))
    caracter= cadena[0]
    ASCII_cadena= ord(cadena)   
    if len(cadena)>1:
        print("cadena muy larga")
    else:
        comprobacion=lambda ASCII_cadena: True if ASCII_cadena<=57 and ASCII_cadena>=48 else False
        if comprobacion(ASCII_cadena):
            print("su caracter es un digito")
        else:
            print("su caracter no es un digito")
            print("se limita a solo una letra para obtener solo un valor evaluable") 
