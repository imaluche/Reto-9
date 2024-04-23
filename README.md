# Reto-9
Reto numero 9 programacion de computadoras


## Ejercicio 1
Seleccione 3 funciones de retos anteriores y escribalas con lambdas
# Funcion 1: Evaluar si un caracter es un digito segun los codigos ASCII (funcion proveniente del tercer punto del reto 4)
```python
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

```
- Declaramos una variable llamada "cadena" de tipo string, esta sera el caracter que vamos a evaluar
- Declaramos otra variable que represente el primer caracter de la cadena, para trabajar unicamente con la primera letra
- Usando la palabra reservada ord transformamos el ASCII a su numero correspondiente
- aplicamos un condicional para evitar que sean ingresados valores con una longitud mayor a 1, pues el codigo se limita a evaluar el valor de un solo caracter
- En caso de que no sea mayor a 1 la cantidad de caracteres usamos un lambda, este lambda arrojara un valor booleando tomando en cuenta el rango de valores de los digitos
- Si esta dentro del valor la variable comprobacion en la que se aplica el lambda sera verdadera, en caso contrario sera falsa
- Aplicamos un ultimo condicional que evalue si la comprobacion es verdadera, si es asi el caracter es un digito, en caso contrario no es posible que lo sea
# Funcion 2: Evaluar si 3 longitudes pueden formar un triangulo (funcion proveniente del sexto punto del reto 4)
```python
#Se trabajara a partir de una funcion que nos dice si 3 longitudes pueden formar un triangulo, es el sexto punto del reto 4
if __name__=="__main__":
 a:float=float(input("valor de la longitud 1:"))
 b:float=float(input("valor de la longitud 2:"))
 c:float=float(input("valor de la longitud 3:"))
 Resulado=lambda a,b,c: True if a+b>c and a+c>b and b+c>a else False
 if Resulado(a,b,c)==True:
  print("se puede hacer un triangulo")
 else:
  print("no se puede hacer un triangulo") 
```
- Declaramos 3 variables introducibles por teclado, cada una representara una de las longitudes a evaluar
- Creamos una variable "resultado" que sea igual a un lambda, este lambda tomando los 3 valores de longitud evaluara si la suma de 2 de ellos es igual a un tercero, sucediendo esto con los 3 casos posibles (a+b>c, a+c>b y b+c>a).
- Si esto se cumple Resultado sera verdadero, en caso contrario sera falso
- Aplicamos una condicional que evalue si resultado es verdadero, si esto es verdad efectivamente se podra hacer un triangulo a partir de las longitudes

# Funcion 3: Evaluar el numero de contagios a partir del numero de contagios actuales y el numero de dias que pasaron (esta funcion es tomada del sexto ejercicio del reto 6)
```python
#Se trabajara a partir de una funcion que nos dice el numero de contagios a partir de un numero de contagios iniciales y un numero de dias
# Este ejercicio es el sexto del reto 6
if __name__=="__main__":
    contagios_hoy:float=float(input("¿cuantos contagios hay al inicio del conteo?"))
    dias:float=float(input("¿cuantos dias se hara la cuenta?"))
    resultado= lambda contagios_hoy,dias: (2**dias)*contagios_hoy
    print("despues de "+ str(dias)+" dias habran "+ str(resultado(contagios_hoy,dias))+" contagios")
```
- Declaramos 2 variables que represente los contagios iniciales y el numero de dias, ambas introducibles por teclado
- Creamos una variable llamada resultado que contega un lambda, este tomara el numero de contagios actuales y los dias y hara una operacion para obtener el numero de contagios finales (se obtiene del producto de 2 potenciado al numero de dias por el numero actual de contagios)
- Imprimimos el resultado de manera entendible

## Ejercicio 2
De los retos anteriores seleccionar 3 funciones y escribirlas usando argumentos no definidos (*args)
# funcion 1: Funcion para obtener el promedio aditivo de una serie de numeros (pertenece al septimo punto del reto 6)
```python
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
```
- Definimos una funcion que no tenga parametros definidos, esta nos permitira ingresar cuantas variables querramos
- Dentro de la funcion declaramos 2 variables que representen el valor de la suma de los valores para el promedio y la cantidad de valores, abmas inicializadas en cero
- Justo despues aplicamos un bucle for que pase por todos los valores dentro de args (los valores ingresados en la funcion), en este por cada paso se le sumara a la variable division 1 (representando que hay 1 valor mas a contar) y se le sumara a resultado el valor a actual de i (representando que se le suma a resultado el valor actual)
- Esto se repetira con todos los valores de i, cuando esto acabe se entregara el valor resultante de la division entre la suma de valores (representacion) y el numero de valores (division)
- Ya dentro del codigo definimos valores (pueden ser los que se deseen, pero en este caso usaremos 5) los cuales seran a los que se les obtendra el promedio, todos estos valores son ingresables por teclado
- Imprimimos el resultado de la funcion con los numeros, dentro del codigo mostrado de ejemplo se aplica la funcion con diferente cantidad de valores para comprobar su efectividad
# Funcion 2:  Funcion para obtener la mediana en una lista de numeros (esta funcion proviene del punto 7 del reto 6)
```python
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

```
- Definimos una funcion que no tenga parametros definidos, esta nos permitira ingresar cuantas variables querramos
- Dentro de la funcion declaramos 2 variables que  represente la tupla de args organizada y la longitud de esta tupla
- Aplicamos un condicional que evalue si la longitud del conjunto es par o impar. Si es par regresara la suma de los 2 valores de en medio entre 2, si es impar regresara el valor de en medio
- Dentro del codigo en si declaramos variables que seran aplicadas en la funcion, estas pueden ser cuantas se deseen (en nuestro caso pondremos solamente 5)
- Imprimimos los resultados de la funcion aplicada en los valores, dentro del codigo mostrado de ejemplo se aplica la funcion con diferente cantidad de valores para comprobar su efectividad
# Funcion 3: Funcion para a partir de un conjunto obtener el numero mayor potenciado al menor
```python
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
```
- Definimos una funcion que no tenga parametros definidos, esta nos permitira ingresar cuantas variables querramos
- Declaramos 2 variables llamadas maximo y minimo, estas contendran los valores maximo y minimo de la tupla args (esto se puede hacer usando las palabras reservadas max y min 
- Hacemos que la funcion regrese el valor maximo potenciado a minimo
- Ya en el codigo declaramos las variables que seran parte de la tupla args, estas pueden ser cuantas quieran pero en nuestro caso solo pondremos 5
- Imprimimos los resultados de la funcion aplicada en los valores, dentro de el codigo mostrado de ejemplo se aplica la funcion con diferente cantidad de valores para comprobar su efectividad
## Ejercicio 3
Usar una funcion recursiva para calcular la operacion de potencia con exponentes naturales
```python
def potencia_recursiva(b,e):
    if e == 0:
        return 1
    else:
        return b * potencia_recursiva(b,e-1)
if __name__=="__main__":
    b:float=float(input("Ingrese la base: "))
    e:float=float(input("Ingrese el exponente: "))
    print("El resultado de la potencia es: ",potencia_recursiva(b,e))
```
- Definimos la funcion para la potencia, en esta se deberan ingresar 2 valores (b para la base y e para el exponente)
- Aplicamos un condicional que evalue el valor de e, si este es igual a 0 podemos asumir que el valor es 1. Por tanto regresandolo
- Si este es cualquier otro valor NATURAL se regresara el producto de la base por la funcion aplicada en la base y el exponente menos 1 
- Ya dentro del codigo declaramos 2 variables introducibles por teclado para la base y el exponente
- Imprimimos el resultado de la funcion aplicada en estas variables de una manera comprensible

## Ejercicio 4
Realizar pruebas para comparar la sucesion de fibonacci con iteracion y recursion por medio de una plantilla que evalue el tiempo que se tarda
```python
import time
def recursofibo(n:int)->int:
      if n <=1:
          return 1
      else:
          return recursofibo(n-1)+recursofibo(n-2)  
def fibonacci(n):
    i:int=0
    n1:int=0
    n2:int=1
    while i<n:
        suma=n1+n2
        n1=n2
        n2=suma
        i+=1
    return suma
if __name__ == "__main__":
    start_timer = time.time()
    global n
    n:int=int(input("Ingrese el numeros de la serie fibonacci: "))
    r=recursofibo(n)
    print(r)
    end_timer = time.time()
    timer = end_timer - start_timer
    print(timer)
    start_timeo = time.time()
    o=fibonacci(n)
    print(o)
    end_timeo = time.time()
    timero = end_timeo - start_timeo
    print(timero)
    print("hay una diferencia de "+str(timer-timero)+" segundos entre los dos metodos")
```
- (No se tomara en cuenta lo que pasa relacionado a time excepto para el final, pues eso no es producto mio)
- Definimos 2 funciones en la que se introduzca una variable que represente el numero de la serie de fibonacci, en cada una usaremos su respectivo metodo (no es necesario explicarlo pues en la clase se explico)
- Ya dentro del codigo declaramos una variable que represente el resultado de los valores, aqui es donde entra a tener importancia el tiempo (en este caso el tiempo se representara por las variables timer y timero, la primera es del metodo recursivo y la segunda del iterativo)
- Declaramos el resultado del metodo recursivo y justo debajo imprimimos el tiempo que tardo (timer), despues imprimimos el resultado del metodo iterativo y justo debajo cuanto se tardo (timero).
- Aclaramos que se imprimen los resultados de las series para comprobar que coincidan
- Imprimimos la diferencia entre ambos valores para tener mas claro la diferencia de tiempo
- Al analizarlo podemos darnos cuenta que el metodo iterativo es el mas rapido

## Ejercicio 5
Crear cuenta de stackoverflow y adjuntar la imagen
![image](https://github.com/imaluche/Reto-9/assets/159048470/d80bcff6-b87d-4cf1-9ce2-6d846f7376b5)
## Ejercicio 6
Crear cuenta en likedin
[Linkedin de Iván Maluche](https://www.linkedin.com/in/iv%C3%A1n-undefined-675b38298/)

