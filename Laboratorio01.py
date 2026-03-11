"""
E: Numero
S: impuesto de renta
R:
"""
def calcularRenta(sal):
    res = 0
    if sal <= 817000:
        return res
    if sal > 817000 and sal <= 1226000:
        por1 = 18300
        res = sal - 18300
        return res
    else:
        por2 = 40900
        por3 = 116000
        pors = por2 + por3
        res = sal - pors
        return res
    return res

"""
E: Numero
S: cantidad de digitos del numero
R: Solo numero enteros
"""
def contadorDigitos(num):
    num = (abs(num))
    res = 0
    if num == 0:
        res += 1
        return res
    while num > 0:
        res += 1
        num = num//10
    return res

"""
E: Numero
S: Cantidad de digitos del numero seleccionado
R: numero y digito deben ser enteros
"""
def contadorDigitos_V2(num, digito):
    num = (abs(num))
    res = 0
    if num == digito:
        res+= 1
        return res
    while num > 0:
        if digito == num %10:
            res += 1
        num = num // 10
    return res
        
