def potencia_recursiva(b,e):
    if e == 0:
        return 1
    else:
        return b * potencia_recursiva(b,e-1)
if __name__=="__main__":
    b:float=float(input("Ingrese la base: "))
    e:float=float(input("Ingrese el exponente: "))
    print("El resultado de la potencia es: ",potencia_recursiva(b,e))