# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 01:10:20 2023

@author: lucas
"""

class Myarray2:
    def __init__(self, elems, r, c, by_row = True):
         self.elems = elems
         self.r = r
         self.c = c
         self.by_row = by_row
         if len(self.elems) != self.r: raise ValueError("La cantidad de elementos no es correcta")
         for filas in self.elems:
             if len(filas) != self.c: raise ValueError("La cantidad de elementos no es correcta")
         
    def get_pos(self, j, k, *args):
        """
        Retorna en que posicion de la matriza se encuentra el elemento de las
        cordenas. La posicion del primer elemento es 1. De la misma manera, tanto
        la fila como la columna son la nuemro 1.
        Parameters
        ----------
        j : int
            Fila donde se encuentra el elemento.
        k : int
            Columna donde se encuentra el elemento
        Returns
        -------
        TYPE Int
            Es la posicion de la matriz donde se ubica la cordenada (j, k).

        """
        if  j<=0 or j>self.r or k<=0 or k>self.c or type(j)!=int or type(k)!=int: raise ValueError(f"La cordenasa no son validas. La matriz es de {self.r}  x {self.c}")
        if self.by_row: salida = (j-1)*self.r + k
        else: salida = (k-1) * self.c +j
        return salida
        #return (j-1)*self.r + k
    
    def get_coords(self, m, *args):
        """
        Deuelve las cordenadas de una posicion dada.
        Parameters
        ----------
        m : int
            Posicion del elemento en la matriz.
        Returns
        -------
        TYPE tuple
            Cordenadas del elemento de la posicion m en la matriz
        """
        if m <= 0 or m >= self.c * self.r or type(m)!=int: raise ValueError(f"Esa posicion no se encuentre en la matriza. Reduerde que la posicion del primer elemento es 1 y la del ultimo {self.r*self.c}")
        if self.by_row:
            fila = (m+1) // self.c 
            columna = self.c if m % self.c == 0 else m % self.c
        else:
            columna = (m+1) // self.r
            fila = self.r if m % self.r == 0 else m % self.r
        return fila,columna
            
            
        # fila = m // self.c
        # columna = m % self.c
        # return (fila+1, columna)
    
    def get_row(self, j, *args):
        """
        Devuelve los elemento de la fila j en la matriz. La primer fila de la matriz es 1, la ultima self.r
        Parameters
        ----------
        j : int
            Numero de fila de la que se desea obtener los elementos.
        Returns
        -------
        list 
            Elementos de la fila j.
        """
        if  j<=0 or j>self.r or type(j)!=int: raise ValueError (f"La fila no se encuentra en la matriz.")
        if self.by_row: salida = self.elems[j-1]
        else: salida = [i[j-1] for i in self.elems]
        return salida
        #return [self.elems[j-1]]
    
    def get_col(self,k):
        """
        Devuelve los elemento de la columna k en la matriz. La primer columna de la matriz es 1, la ultima self.c
        Parameters
        ----------
        k : int
            Numero de columna de la que se desea obtener los elementos.
        Returns
        -------
        list 
            Elementos de la columna k.

        """
        if  k<=0 or k>self.c or type(k)!=int: raise ValueError (f"La columnano se encuentra en la matriz.")
        if self.by_row: salida = [lista[k-1] for lista in self.elems]
        else: salida = self.elems[k-1]
        return salida
        #return [lista[k-1] for lista in self.elems]
        
    def get_elem(self, j, k, *args):
        """
        Decvuele el valor del elemento de las cordenas c.
        Parameters
        ----------
        c : tuple
            Cordenadas del elemnto de la matriz.
        Returns
        -------
        int
            Valor del elemento que se encuentr en las codernadas c.
        """
        if  j<=0 or j>self.r or k<=0 or k>self.c or type(j)!=int or type(j)!=int: raise ValueError(f"La cordenasa no son validas. La matriz es de {self.r}  x {self.c}")
        if self.by_row: salida = self.elems[j-1][k-1]
        else: salida = self.elems[k-1][j-1]
        #return self.elems[j-1][k-1]
    
    def del_row(self, j, *args):
        """
        Elimina la fila j y retorna un objeto que contenga la matriz sin esta fila.
        
        Parameters
        ----------
        j : int
            Nuemro de fila que se desea eliminar.
        Returns
        -------
        TYPE Myarray2
            Objeto identico, pero la matriz no tiene la fila j.

        """
        if  j<=0 or j>self.r or type(j)!=int: raise ValueError (f"La fila no se encuentra en la matriz.")
        if self.by_row: salida = Myarray2(self.elems[:j-1] + self.elems[j:], self.r-1, self.c)
        return Myarray2(self.elems[:j-1] + self.elems[j:], self.r-1, self.c)
    
    def del_col(self, k, *args):
        """
        Elimina la columna k y retorna un objeto que contenga la matriz sin esa columna.
        Parameters
        ----------
        k : int
            Numero de la columna que se desea eliminar.
        Returns
        -------
        TYPE Myarray2
            Objeto identico, pero la matriz no tiene la columna k

        """
        if  k<=0 or k>self.c or type(k)!=int: raise ValueError (f"La columnano se encuentra en la matriz.")
        return Myarray2([i[:k-1] + i[k:]  for i in self.elems], self.r, self.c-1)
    
    def scale_row(self, j, x, *args):
        """
        
        Parameters
        ----------
        j : int
            Fila que se multiplicara por el escalar x.
        x : int/Float
            valor del escalar por el que se multiplicara la fila j.

        Returns
        -------
        TYPE Myarray2
            Objeto identico, pero con la fila j multiplicada por el escalar x.

        """
        if j<=0 or j>self.r or type(j) != int: raise ValueError(f"La fila no se encuentra en la matriz.")
        aux = [fila[::] for fila in self.elems]
        aux[j-1] = [elemento*x for elemento in aux[j-1]]
        print(aux, self.r, self.c)
        return Myarray2(aux, self.r, self.c)
    
    def scale_col(self, k, y, *args):
        """
        
        Parameters
        ----------
        k : Int
            Columna que se multiplicara por el escalar y.
        y : Int/Float
            Valor del escalar por el qeu se multiplkicara la columna k.
        Returns
        -------
        aux : Myarray2
            Objeto identico, pero con la columna k multiplicada por el escalr y.

        """
        if k<=0 or k>self.c or type(k) != int: raise ValueError(f"La fila no se encuentra en la matriz.")
        aux = [fila[::] for fila in self.elems]
        c=0
        for fila in aux:
            aux[c][k-1] = fila[k-1] * y
            c += 1
        return Myarray2(aux, self.r, self.c)
    
    def swap_rows(self, j, k, *args):
        """
        Intercambia laas filas j y k de la matriz. Devuelve un objeto con los mismos atributos pero con las filas j y k intercambiadas entre si.
        Parameters
        ----------
        j : Int
            Fila a intercambiar por k.
        k : TYPE
            Fila a intercambiar por j.
        Returns
        -------
        TYPE Myarray2
            Objeto identico, pero la matriz tiene intercambiadas las filas j y k.
        """
        if  j<=0 or j>self.r or k<=0 or k>self.r or type(j)!=int or type(k)!=int: raise ValueError(f"Las filas no son validas,a matriz es de {self.r}  x {self.c}")
        aux = self.elems.copy()
        fila_j, fila_k = aux[j-1], aux[k-1]
        aux[j-1], aux[k-1] = fila_k, fila_j
        return Myarray2(aux, self.r, self.c)
    
    def swap_cols(self, k, y, *args):
        """
        Intercambia las columnas k & y de la la matriz. Devuelve un objeto con los mismos atributos pero con las columnas k & y intercambiadas entre si.
        Parameters
        ----------
        k : int
            Columna a intercambiar por y.
        y : int
            Columna a intercambiar por k.
        Returns
        -------
        TYPE Myarray2
            Objeto indentico, pero la matriz tiene intercambiadas las filas k & y.
        """
        if  y<=0 or y>self.c or k<=0 or k>self.c or type(y)!=int or type(k)!=int: raise ValueError(f"La columnas no son validas, a matriz es de {self.r}  x {self.c}")
        aux = [fila[::] for fila in self.elems]
        columna_k, columna_y =[], []
        for i in range(self.r):
            aux[i][k-1] = self.elems[i][y-1]
            aux[i][y-1] = self.elems[i][k-1]
        return Myarray2(aux, self.r, self.c)
    
    def transpose(self, *args):
        """
        Calcula la transpuesta de la matriz y devuelve un objeto con esta.
        Returns
        -------
        TYPE Myarray2
            Objeto que contiene la matriz transpuesta.
        """
        aux = self.elems.copy()
        r = self.r
        salida = []
        for i in range(r):
            columnas = []
            for fila in aux:
                columnas.append(fila[i])
            salida.append(columnas)
        print(self.r, self.c)
        print(len(salida))
        return Myarray2(salida, r, self.c)
    
    def flips_rows(self, *args):
        """
        Cre un nuevo objeto con una matriz que refleje especularmente las filas.
        Returns
        -------
        aux : Myarray2
            Objeto con los mismos atributos pero con las filas de la matriz reflejados especularmente.
        """
        aux = Myarray2(self.elems, self.r, self.c)
        for i in range(1, self.r//2+1):
            aux = aux.swap_rows(i, self.r-i+1)
        return aux
    
    def flips_cols(self, *args):
        """
        Crea un nuevo objeto con una matriz que refleje especularmente las columnas.
        Returns
        -------
        aux : Myarray2
            Objeto con los mismos atributos pero con las columnas de la matriz reflejados especularmente.
        """
        aux = Myarray2(self.elems, self.r, self.c)
        for i in range(1, self.c//2+1):
            aux = aux.swap_cols(i, self.c-i+1)
        return aux
    
    def shift(self, d, c, *args):
    
        """
        Mueve en la dirececion c la cantida d las filas/columnas de una matriz.
        Parameters
        ----------
        d : Str
            Direccion en la que se mueven los elementos.
        c : Int
            Cantidad de lugares que se mueve.
        Returns
        -------
        TYPE Myarray2
            Devuelve un objeto que contenga la matriz con los elementos desplazados a la direccion {d} {c} veces.

        """
        if d[0].lower() not in "rlud": raise ValueError(f"{d} no es una direccion valida o {c} no es una cantidad valida, ingrese otra.")
        aux = []
        if d[0].lower() == "d":
            aux = self.elems[-c:] + self.elems[:-c]
        elif d[0].lower() == "u":
            aux = self.elems[c:] + self.elems[:c]
        elif d[0].lower() == "r":
            for fila in self.elems:
                aux.append( fila[self.c-c:] + fila[:self.c-c] )
        elif d[0].lower() == "l":
            for fila in self.elems:
                aux.append( fila[c-self.c:] + fila[:c-self.c])
        return Myarray2(aux, self.r, self.c)
        
    def det_1(self, *args):
        """
        Calcula el determinante de una matriz dada.
        Parameters
        ----------
        Returns
        -------
        dete : Float
            Determinante de la matriz.

        """
        if self.r != self.c: raise ValueError(f"La matriz debe ser cuadrada(NxN) para poder calcular el determinante")
        aux = Myarray2(self.elems, self.r, self.c)
        sub_matriz = Myarray2(self.elems, self.r, self.c)
        dete = 0
        if self.r == 2:
            dete = aux.get_elem(1,1) * aux.get_elem(2,2) - aux.get_elem(1,2) * aux.get_elem(2,1)
        else:
            for i in range(0, self.r):
                n = aux.get_elem(1,i+1)
                sub_matriz = aux.del_col(i+1)
                sub_matriz = sub_matriz.del_row(1)
                dete += sub_matriz.det_1() * n * (-1) ** (i)
        return float(dete)
    
    def myprint(self):
        for i in range(0,self.r):
            print(self.elems[i])
        return None

    
matriz = Myarray2([[1,2,3,5],
              [4,5,6,5],
              [7,8,95,5],
              [10,11,12,500]],4,4)

a=matriz.get_coords(8)
#%%

if __name__ == "__main__":
    
    matriz = Myarray2([[1,2,3,5],
                  [4,5,6,5],
                  [7,8,95,5],
                  [10,11,12,500]],4,4)
    
    #Atributos
    print(matriz.elems)
    print(matriz.r)#Cantidad de filas
    print(matriz.c)#Cantidad de columnas
    print("-----------------------------")

    #Get_pos
    print(matriz.get_pos(3,1))
    #print(matriz.get_pos(5,5))#Las cordenadas no eexiste
    print("-----------------------------")

    #Get_row
    print(matriz.get_row(2))
    #print(matriz.get_row(5))#No existe la fila 5
    print("-----------------------------")

    #Get_col
    print(matriz.get_col(2))
    #print(matriz.get_col(5))#No existe la columna 5
    print("-----------------------------")

    #Get_elem
    print(matriz.get_elem(3,3))
    #print(matriz.get_elem(1,6))#No esxite la columna 6
    print("-----------------------------")
    
    #del_row
    matriz_2 = matriz.del_row(2)
    matriz_2.myprint()
    #matriz_2 = matriz.del_row(5)#Tira error porque no exixte la fila 5
    print("-----------------------------")
    
    #del_col
    matriz_3 = matriz.del_col(3)
    matriz_3.myprint()
    #matriz_3 = matriz.del_col(8)#Tira error, no existe la columna 8
    print("-----------------------------")
    
    #Swaps_rows
    matriz_4 = matriz.swap_rows(2, 3)
    matriz.myprint()
    print("---")
    matriz_4.myprint()
    print("-----------------------------")
    
    #Swap_cols
    matriz_5 = matriz.swap_cols(2, 3)
    matriz.myprint()
    print("---")
    matriz_5.myprint()
    print("-----------------------------")
    
    #Scale_rows
    matriz_6 = matriz.scale_row(3,2)
    matriz.myprint()
    print("---")
    matriz_6.myprint()
    print("-----------------------------")
    
    #Scale_cols
    matriz_7 = matriz.scale_col(3,2)
    matriz.myprint()
    print("---")
    matriz_7.myprint()
    print("-----------------------------")
    
    #Transpoce
    matriz_8 = matriz.transpose()
    matriz.myprint()
    print("---")
    matriz_8.myprint()
    print("-----------------------------")
    