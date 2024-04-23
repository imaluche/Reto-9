#se usara una funcion para obtener la mediana de una lista de numeros, esta funcion viene del punto 7 del reto 6
def mediana(*args):
    sorted_args = sorted(args)
    n = len(sorted_args)
    if n // 2 == n/2:
        return (sorted_args[n//2 - 1] + sorted_args[n//2]) / 2
    else:
        return sorted_args[n//2]
if __name__=="__main__":
    a:float=float(input("ingrese el primer numero: "))
    b:float=float(input("ingrese el segundo numero: "))
    c:float=float(input("ingrese el tercer numero: "))
    d:float=float(input("ingrese el cuarto numero: "))
    e:float=float(input("ingrese el quinto numero: "))
    print("la medidana de los primeros 2 numeros es: ",mediana(a,b))
    print("la medidana de los primeros 3 numeros es: ",mediana(a,b,c))
    print("la medidana de los primeros 4 numeros es: ",mediana(a,b,c,d))
    print("la medidana de los 5 numeros es: ",mediana(a,b,c,d,e))
