# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:26:26 2023

@author: lucas
"""

class FF():
    """ Documentacion que va al __doc__ del objeto
        Poner aqui lo que se quiera explicar en un help.
        Por una cuestion de seguridad, vamos a usar tuplas 
        para garantizar la inmutabilidad del objeto
        """
    def __init__(self,tupla=tuple()):
        self.flujos=tupla
        
    def van(self,tasa, n=0):
        """ Calculo de valor actual neto recursivo
            Inputs: 
                1 - tasa (posicional)
                2 - n posicion en el vector ( default = 0, named argument ). 
                    Sirve para manejar recursivamene las iteraciones 
                    sin alterar la lista del flujo de fondos  
        """
        if len(self.flujos)>0:
            if n==len(self.flujos):
                salida = 0
            else:
                salida = self.flujos[n]+1.0/(1.0+tasa)*self.van(tasa, n=n+1)
        else:
            print('\n',"La tupla de flujo de fondos esta vacia. Se devuelve 0")
            salida = 0
        return salida
    
    def vt(self,tasa,t = 0):
        """ Calculo de valor del flujo de fondos a un tiempo t
            Funciona calculando van y luego llevando a tiempo t correspondiente
            Inputs: 
                1 - tasa (posicional)
                2 - t momento de valuacion ( default = 0, named argument ). 
                    
        """
        return self.van(tasa)*(1.0+tasa)**t
    
    def tir_GS(self, a = 0, b = 1, n = 110, t = 1/100):
        particiones = []
        c = 0
        
        while len(particiones) != n+1:
            particiones.append(a +(b-a)/n*c)
            c += 1
            a += t
        validas = []
        
        for i in range(1, len(particiones)):
            a, b = particiones[i-1], particiones[i]
            if 1 + a == 0: a += t
            if 1 + b == 0: b += t
            if self.van(a) * self.van(b) <= 0:
                validas.extend([a, b])

        if -t < self.van(a) - self.van(b) < t:
            tir = (validas[0] + validas[1])/2
        else:
            tir = self.tir_GS(validas[0],validas[1])
        return round(tir, 3)
    
    def tir_BI(self, a=-2, b=2):
        t = 1/100000 #Margen de error
        if 1+a == 0: a+=t
        elif 1+b == 0: b+=t
        if -t < self.van(b) - self.van(a) < t:
            tir = (b+a) / 2
        else:
            c = a + (b - a) / 2 #Donde se parte el intervalo
            if self.van(a) * self.van(c) < 0:
                tir = self.tir_BI(a, c)
            elif self.van(c) * self.van(b) < 0:
                tir = self.tir_BI(c, b)
        return round(tir,3)
    
    def tir_AS(self, r = 0, h = 1/100):
        if self.van(r) > self.van(h+r):
            if self.van(r) * self.van(h+r) < 0 : tir = self.tir_BI(r, r+h)
            else:
                r += h
                tir = self.tir_AS(r+h, h)
        return tir

flujos = FF([-50, 5, 5, 5, 5, 55])
a=flujos.tir_GS(0,1)