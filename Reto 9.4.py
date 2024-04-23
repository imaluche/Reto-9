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