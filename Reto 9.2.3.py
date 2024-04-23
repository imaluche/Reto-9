#Se usara una funcion para a partir del maximo y minimo de un conjunto de numeros se obtenga el mayor potenciado al menor
def potencia(*args):
    maximo = max(args)
    minimo = min(args)
    return maximo**minimo
if __name__=="__main__":
    a:float=float(input("Ingrese el primer numero: "))
    b:float=float(input("Ingrese el segundo numero: "))
    c:float=float(input("Ingrese el tercer numero: "))
    d:float=float(input("Ingrese el cuarto numero: "))
    e:float=float(input("Ingrese el quinto numero: "))
    print("El resultado de la potencia con los primeros 2 numeros es: ",potencia(a,b))
    print("El resultado de la potencia con los primeros 3 numeros es: ",potencia(a,b,c))
    print("El resultado de la potencia con los primeros 4 numeros es: ",potencia(a,b,c,d))
    print("El resultado de la potencia con los 5 numeros es: ",potencia(a,b,c,d,e))