# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:48:21 2022

@author: Leonardo Falango
"""


#===================================================== Ex 1 =====================================================


def areaCirculo(raio):
    import math
    if raio <= 0:
        int("a")
    area = math.pi*(raio**2)
    return area


try: 
    raio = float(input("Entre com o valor do raio: "))
    areacirculo = areaCirculo(raio)
    print("A area do círculo é: {:.02f}".format(areacirculo))
except ValueError:
    print("ERRO. Valor inválido")
    
 
    
 
    
#===================================================== Ex 2 =====================================================
 
    
def RNA(DNA):
    RNA = []
    for i in range(len(DNA)):
        if DNA[i].lower() == "g":
            RNA.append("C")
        elif DNA[i].lower() == "c":
            RNA.append("G")
        elif DNA[i].lower() == "t":
            RNA.append("A")
        elif DNA[i].lower() == "a":
            RNA.append("U")
        else:
            forceError = int("a") # ENTRE APENAS COM C G T A
            return forceError
    return RNA


elementoDna = input("Entre com a sequência de nucleotídeos (ex: G C T A G G A T)")
cadeia = elementoDna.split(" ")
print(RNA(cadeia))



#===================================================== Ex 3 =====================================================

def Bhaskara(a, b, c):
    # x = -b +- (b² - 4 ac / 2) / 2a
    #Sao três casos: 1 -> delta positivo (2 raízes reias) delta zero (uma raiz real) e delta negativo (nenhuma raíz real)
    delta = (b**2) - (4*a*c)

    if delta == 0:
        x1 = -b / (2*a)
        x2 = x1
        print(f"Teremos 1 raiz: {x1}")
        return x1,x2 #Caso queira fazer contas com x1,x2 retornaremos os numeros, para usa-los 'x,y = Bhaskara(a,b,c)'
    elif delta > 0:
        x1 = (-b + (delta**(1/2))) / (2 * a)
        x2 = (-b - (delta**(1/2))) / (2 * a)
        print(f"Teremos 2 raizes: {x1} e {x2}")
        return x1,x2
    else:
        print("Não há raízes")
        return False #Se der Type error, quer dizer que não ha raízes






try:
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))
    
    Bhaskara(a, b, c)
except ValueError:
    print("ERRO. Entre com valores float.")
except ZeroDivisionError:
    print("ERRO. Entre com valores válidos")


#===================================================== Ex 4 =====================================================

def ehanagrama(str1, str2):
    if len(str1) == len(str2):
        listaLetras = []
        listaLetras2 = []
        
        for i in range(len(str1)):
            listaLetras.append(str1[i])
            listaLetras2.append(str2[i])
        listaLetras.sort()
        listaLetras2.sort()
        for i in range(len(str1)):
            if listaLetras[i]== listaLetras2[i]:
                continue
            else: return False
        return True

    else:
        return False


entrada1 = input("Entre com a primeira String: ")
entrada2 = input("Entre com a segunda String: ")
print("É anagrama? {}".format(ehanagrama(entrada1,entrada2)))

#===================================================== Ex 5 =====================================================

def verificaIP(ip):
    ips = ip.split(".")
    if len(ips) > 4 or len(ips) < 3:
        return False
    try:
        for i in range(len(ips)):
            if int(ips[i]) < 1000 and int(ips[i]) > 0:
                pass
            else:
                return False
        return True
    except ValueError:
        return False


ip = input("Entre com o endereço de ip: ")
existe = verificaIP(ip)
print(existe)


#===================================================== Ex 6 =====================================================


def fatorial(x):
    lista = []
    fatorial = 1
    fat = x
    while fat >= 1:
        lista.append(fat)
        fat -= 1
    for i in range(len(lista)):
        numero = lista[i]
        fatorial = fatorial * numero
    print(f"O fatorial de {x} = {fatorial}")
    return lista,fatorial

try:
    x = int(input("Entre com o valor de x: "))
    lista, total = fatorial(x)
    print("O valor de {}! = {}\nTotal: {}".format(x, lista, total))

except ValueError:
    print("Erro. Valor invalido")


