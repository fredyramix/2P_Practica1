# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random


def primera_generacion(variables):
    #variables[0] = funcion
    #variables[1] = numero de cromosomas
    #variables[2] = numero de generaciones
    #variables[3] = minimo
    #variables[4]=maximo
    #variables[5]=max o min donde max = 1 & min = 0
    ind_iniciales={} #declaramos un diccionario de invididuos iniciales
    individuos={}
    max=len(bin(int(variables[4])))-3
    for x in range(1,int(variables[1])+1):
            v=random.randrange(int(variables[3]),int(variables[4])+1)
            bini=bin(v)
            g=len(bini)
            cade=bini[2:g]
            cromosoma=[]
            for h in cade:
                cromosoma.append(h)
            while len(cromosoma)<=max:
                cromosoma.insert(0,0)
            individuos[str(x)]=cromosoma
    return individuos

def ImprimePrimeraGeneracion(cromos):
    print "N° \t\tCodificacion"
    a=cromos.items()
    for x in a:
        print ""+str(x[0]) +"\t\t"+ str(x[1])
def ImprimeProbabilidad(cromos):
    print "N° \t\tCodificacion \t\tEntero   \t\tF(X)\t\t\tPenalizacion\t\tProbabilidad Invertida"
    for x in cromos:
        print ""+str(x[0]) +"\t\t"+ str(x[1]) +"\t\t\t"+ str(x[2]) +"\t\t\t\t"+ str(x[3])+"\t\t\t"+ str(x[4])+ "\t\t\t"+ str(x[5])
def ImprimeParejas(parejas):
    print "N° \t\tCodificacion \t\tEntero   \t\tF(X)\t\t\tPenalizacion\t\tProbabilidad Invertida"
    for x in parejas:
        print ""+str(x[0]) +"\t\t"+ str(x[1]) +"\t\t\t"+ str(x[2]) +"\t\t\t\t"+ str(x[3])+"\t\t\t\t"+ str(x[4])+ "\t\t\t\t"+ str(x[5])
def ImprimePenalizacion(cromos):
    print "N° \t\tCodificacion \t\tEntero   \t\tF(X)\t\t\tPenalizacion"
    for x in cromos:
        print ""+str(x[0]) +"\t\t"+ str(x[1]) +"\t\t\t"+ str(x[2]) +"\t\t\t\t"+ str(x[3])+"\t\t\t"+ str(x[4])

def Calculo_fx(resultado):
    r=resultado.items()
    r.sort()
    #print "Calculo de f(x):"
    #print "N° \t\tCodificacion \t\tEntero   \t\tF(X)"
    ind=[]
    count=1
    for x in r:
        indi=[]
        concat=""
        for y in range(0,len(x[1])):
            concat += str(x[count][y])
        entero=int(concat,2)
        fx=entero**2
        indi.append(x[0])
        indi.append(concat)
        indi.append(entero)
        indi.append(fx)
        #print str(x[0])+"\t\t"+concat+"\t\t\t\t"+str(entero)+"\t\t\t\t"+str(fx)
        ind.append(indi)
    return ind

def Penalizar(cromo,variables):
    cromos=[]
    min=variables[3]
    max=variables[4]
    for i in cromo:
        x=i[2]
        if int(x)>=int(min) and int(x) <=int(max):
            i.append(i[3])
        else:
            #print "Entro a penalizar"
            if variables[5]==1:
                i.append(i[3]+1000000)
                #print "penalizo a un maximo"
            else:
                #print "penalizo a un minimo"
                i.append(i[3]-10000000)
        cromos.append(i)
    return cromo
def ImprimeGeneracion(generacion):
    a=generacion.items()
    a.sort()
    print "N°\t\tValor Entero\t\tCodificación"
    for x in a:
        print str(x[0])+ str(x[0][1])
def SumatoriaFX(lista):
    suma=0
    for x in lista:
        suma=suma+abs(int(x[4]))
    return suma
def Probabilidad(sum,individuos):
    for x in individuos:
        resta=float(sum)-float(x[4])
        p=(resta*100)/float(sum)
        x.append(int(p))
    return individuos
def Ruleta(lista):
    rul=[]
    for x in lista:
        x.reverse()
        rul.append(x)
    rul.sort()
    new=[]
    for y in rul:
        y.reverse()
        new.append(y)
    return new


def SeleccionParejas(opciones,variables):
    count =0
    tabla_hijos=[]
    while count!=(int(variables[1])):
        n=random.randrange(0,100)
        for x in opciones:
            if int(x[5]) <= n:
                tabla_hijos.append(x[1])
                count=count+1
                break
            else:
                pass
    return opciones,tabla_hijos

def GenerarLlaves(nueva_generacion):
    diccionario={}
    count = 1
    for x in nueva_generacion:
        diccionario[str(count)]=x
        count=count+1
    return  diccionario
