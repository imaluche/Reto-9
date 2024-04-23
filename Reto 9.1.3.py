#Se trabajara a partir de una funcion que nos dice el numero de contagios a partir de un numero de contagios iniciales y un numero de dias
# Este ejercicio es el sexto del reto 6
if __name__=="__main__":
    contagios_hoy:float=float(input("¿cuantos contagios hay al inicio del conteo?"))
    dias:float=float(input("¿cuantos dias se hara la cuenta?"))
    resultado= lambda contagios_hoy,dias: (2**dias)*contagios_hoy
    print("despues de "+ str(dias)+" dias habran "+ str(resultado(contagios_hoy,dias))+" contagios")