#Se usara la funcion para obtener el promedio aditivo de una serie de numeros, es el punto 7 del reto 6
def potencia2(*args):
    resultado:int=0
    division:int=0
    for i in args:
        division=division+1
        resultado+=i
        return (resultado/(division))
if __name__=="__main__":
    a:float=float(input("valor 1:"))
    b:float=float(input("valor 2:"))
    c:float=float(input("valor 3:"))
    d:float=float(input("valor 4:"))
    e:float=float(input("valor 5:"))
    print("el promedio aditivo de a y b es: "+str(potencia2(a,b)))
    print("el promedio aditivo de a,b y c es: "+str(potencia2(a,b,c)))
    print("el promedio aditivo de a,b,c y d es: "+str(potencia2(a,b,c,d)))
    print("el promedio aditivo de a,b,c,d y e es: "+str(potencia2(a,b,c,d,e)))