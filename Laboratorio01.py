"""
Nombre: calculadora
Entradas: operacion y operadores
Salidas:resultado de la operacion
Restricciones: numeros enteros
"""
def calculadora(operacion,op1,op2):
    if not isinstance (operacion,int):
        return "Error: la operacion debe ser numero entero"
    if not isinstance (operacion,int):
        return "Error: el operador 1 debe ser numero entero"
    if not isinstance (operacion,int):
        return "Error: el operador 2 debe ser numero entero"
    if ((operacion ==4)and (op2==0)):
        return "Error: no se puede dividir entre 0"
    if not ((operacion==1)or(operacion==2) or (operacion==3) or(operacion==4)):
        return "Error, el numero de operador no es valido"
    return calculadora_Aux(operacion,op1,op2)
def calculadora_Aux(operacion,op1,op2):
    resultado=0
    if (operacion==1):
        resultado=(op1+op2)
        
    if (operacion==2):
        resultado=(op1-op2)
      
    if (operacion==3):
        resultado=(op1*op2)
        
    if (operacion==4):
        resultado=(op1//op2)
    return resultado
"""
Nombre: contarDigitos
Entradas: un numero y un digito
Salidas:numero de veces qu el digito sale en el numero
Restricciones: numero y digito enteros, el digito debe ser menor  10 Y mayor o igual a 0
"""
def contarDigitos(num,digito):
    if not isinstance (num,int):
        return "Error: el numero debe ser entero"
    if not isinstance (digito,int):
        return "Error: el digito debe ser numero entero"
    if ((digito>9)or(digito<0)):
        return "Error: el digito debe ser mayor o igual a 0 y menor a 10"
    if (num<0):
        num*=-1
    return contarDigitos_Aux(num,digito)
def contarDigitos_Aux(num,digito):
    digito2=0
    resultado=0
    while num!=0:
        digito2=num%10
        if (digito2==digito):
            resultado+=1
        num= num//10
    return resultado

"""
Nombre:sumatoria_V2
Entradas: inicio, fin, distancia, excepcion
Salidas: suma total de los números desde el parámetro inicio hasta el final.
Restricciones:
Todos parámetros deben ser de tipo entero.
Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0.
Los valores de inicio y fin deben ser positivos
Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
Si excepcion es igual a cero, se debe ignorar este valor, lo contrario, todo número dentro de la secuencia entre inicio y ** final** sea divisible por esta excepcion debe omitirse en la suma
"""
def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not isinstance (inicio,int):
        return "Error: el inicio debe ser numero entero"
    if not isinstance (fin,int):
        return "Error: el fin debe ser numero entero"
    if not isinstance (distancia,int):
        return "Error: la distancia debe ser  numero entero"
    if not isinstance (excepcion,int):
        return "Error: la exepcion debe ser numero entero"   

    if  not ((distancia<10)or(distancia>0)) and ((distancia>-10)or(distancia<0)):
        return "Error: la distancia debe estar entre -9 y 9 sin incluir al 0"

    if ((excepcion>9)or(excepcion<0)):
        return "Error: la exepcion debe ser mayor o igual a 0 y menor a 10"
    if ((inicio<0)or (fin<0)):
        return "Error: el inicio y fin deben ser positivos"

    return sumatoria_V2_Aux(inicio, fin, distancia, excepcion)


def sumatoria_V2_Aux(inicio, fin, distancia, excepcion):
    resultado=0
    while inicio<=fin:
        resultado=inicio
        if excepcion==0:
            resultado+=inicio
        elif inicio%excepcion==0:
            resultado+=inicio
        inicio+=distancia
    return resultado
    
