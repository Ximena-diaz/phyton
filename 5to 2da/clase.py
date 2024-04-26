
nota1=int(input("ingrese la primera nota: "))
nota2=int(input("ingrese su segunda nota: "))
nota3=int(input("ingrese su tercera nota: "))
prom=(nota1+nota2+nota3)/3

if prom >= 7:
    print("esta aprobado")

else: 
  if prom >= 4:
    print("esta regular")
  else:
     print("esta reprobado")
 
