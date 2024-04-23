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