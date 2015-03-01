# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from math import cos,sin
def EvaluarConElite(dict,variables,best):
    #print "Entro a maximizar"
    a=primera(dict,variables)
    a.sort()
    a.reverse()
    #print a
    b=a[0]
    if len(best)==0:
        best=b[:]
    else:
        if variables[5]=='1':
            #maximo
            if int(b[0])>int(best[0]):
                best=b[:]
        else:
            #minimo
            if int(b[0])<int(best[0]):
                best=b[:]
    return best


def primera(resultado,variables):
    #x^2
    if variables[5]=='1' or variables[5]=='0' :
        #maximizar
        r=resultado.items()
        r.sort()
        ind=[]
        count=1
        for x in r:
            indi=[]
            concat=""
            for y in range(0,len(x[1])):
                concat += str(x[count][y])
            entero=int(concat,2)
            if variables[0]=='1':
                fx=entero**2
            elif variables[0]=='2':
                fx=sin(float(entero)) * 40
            elif variables[0]=='3':
                fx=cos(float(entero)) + entero
            elif variables[0]=='4':
                fx=(1000/abs(50-entero))+entero
            elif variables[0]=='5':
                fx=((1000/abs(30-entero))+(1000/abs(50-entero))+(1000/abs(80-entero)))+entero
            #indi.append(x[0])
            indi.append(fx)
            #indi.append(concat)
            indi.append(entero)
            ind.append(indi)
        return ind




