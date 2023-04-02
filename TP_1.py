# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 02:21:32 2023

@author: lucas
"""
#%%
class Myarray:
    def __init__(self, elems, r, c, by_row = True):
         self.elems = elems
         self.r = r
         self.c = c
         self.by_row = by_row
         if self.r * self.c != len(self.elems): raise ValueError("La cantidad de elementos no es correcta")
    
    def get_pos(self, k, j,*args):
        """
        La funcion recibe como parametros las cordenadas de un elemento de la matriz
        y retornara la posicion del elemento. Es indistinto en que manera se ordena la fila (by_row = True or False).
        Parameters
        ----------
        k : int
            Es la fila del elemento al que se le desa obtener la posicion.
        j : int
            .Es la columna del elemento al que se le desa obtener la posicion.

        Returns
        -------
        salida : int
            Es el numero del elemento de la matriz de las coordenadas dadas. El numero de
            posicion de la matriz comienza en el 1.

        """        
        if k <= 0 or k > self.r or j <= 0 or j > self.c: raise ValueError(f"Las cordenadas no estan dentro del rango de la matriz. La matriz es {self.r}x{self.c}")
        r, c = self.r, self.c
        if self.by_row:
            salida = k*c - (c-j)
        else:
            salida = j*r - (r-k)
        return salida
    
    def get_coords(self, m, *args):
        if m<=0 or m>len(self.elems): raise ValueError( f"El elemento n {m} no existe)")
        if self.by_row:
          j, k = m // self.c + 1, m % self.c + 1
        else:
          j, k = m % self.r + 1, m // self.r + 1
        return (j, k)
    
    def switch(self, *args):
        """
        Cambia el formato y las posiciones de la lista elems. Se encarga de que en caso de que tengas
        la lista elems ordenadas por filas la ordene por columnas y viceversa. Al mismo timempo, cambia 
        el valor de by_row, si antes era True despues de utilizar el metodo sera False.
        Returns
        -------
        TYPE Myarray
            Devuelve un objeto con la misma matriz pero con los atributos elems y by_row cambiados

        """
        n_elems = []
        columna_numero = 0#esta es la columna , pero al comenzar con indice 0, al comienzo toma valor 0
        if self.by_row == False:
            e = self.r
            by_row = True
        else:
            e = self.c
            by_row = False
        while columna_numero < e:#cada vez que pasa por el ciclo se mueve una columna a la derecha para agarrar sus elementos
            [n_elems.append(elemento) for elemento in (self.elems[columna_numero::e])]
            columna_numero += 1
        #self.elems = n_elems le mandaba esto como parametro
        # if self.by_row == True:
        #     self.by_row = False
        # else:
        #     self.by_row = True
        return Myarray(n_elems, self.r, self.c, by_row)
    
    def get_col(self, j, *args):
        """
        Devueleve el contendido que hay dentro de la columna j de la matriz. Devuelve una lista
        con todos los valores de la columna j.Es indistinto en que manera se ordena la fila 
        (by_row = True or False).
        Parameters
        ----------
        j : int
            Es el numero de la columna que se desaa obtener.

        Returns
        -------
        salida : list
            Es la columna j de la matriz.

        """
        if j <= 0 or j > self.c: raise ValueError(f"Ingrese otro valor. La matriz es de {self.c} columnas")
        salida = []
        switch = 0
        if self.by_row:
            salida = self.elems[j-1 :: self.c]
            switch = 1
        else:
            for i in range(j-1, len(self.elems), self.c):
                salida.append(self.elems[i])
        if switch==1: self.switch()
        return salida
    
    def get_row(self, k, *args):
        """
        Devueleve el contendido que hay dentro de la fila k de la matriz. Devuelve una lista
        con todos los valores de la fila k.Es indistinto en que manera se ordena la fila (by_row = True or False).
        Parameters
        ----------
        j : Int
            Es el numero de la fila que se desea obtener.

        Returns
        -------
        salida : list
            Es la fila j de la matriz."""
        if k<=0 or k > self.r: raise ValueError(f"Ingrese otro valor. La matriz es de {self.r} filas")
        switch = 0
        if self.by_row == False:
            self.switch()
            switch = 1
        salida = self.elems[(k-1)*self.c:k*self.c]
        self.switch()
        if switch==1: self.switch()
        return salida
    
    def get_elem(self, j, k, *args):
        """
        La funcion recibe como parametros las cordenas de un elemento de la matriz y devuelve el valor
        del elemento de esas cordenadas
        Parameters
        ----------
        j : int
            Es el numero de la fila del elemento que se desea obtener.
        k : int
            Es el numero de la fila del elemento que se desea obtener.

        Returns
        -------
        salida : int
            Es el elemento de la matriz qeu se ubica en las cordenas (j, k).

        """
        if k <= 0 or k > self.c or j < 0 or j >self.r: raise ValueError(f"Las cordenasa no estan dentro del rango de la matriz. La matriz es {self.r}x{self.c}")
        
        
        # switch = 0
        # indice = ((j-1)*self.c + k)-1
        # if self.by_row == False:
        #     self.switch()
        #     switch = 1
        #     indice = (j-1)*self.r
        # salida = self.elems[indice]
        # if switch==1: self.switch()
        return self.elems[((j-1)*self.c+k-1)] if self.by_row==True else self.elems[((k-1)*self.r+j)]
    
    def del_row(self, j, *args):
        """
        Se encarga de crear un nuevo objeto con la misma matriz pero sin la fila j.Es indistinto en que
        manera se ordena la fila (by_row = True or False).
        Parameters
        ----------
        j : int
            Es el numero de fila que se desa eliminar de la matriz.

        Returns
        -------
        TYPE Myarray
            Es un objeto similar a elems pero sin la fila j y con r = r-1.

        """
        if j<=0 or j>self.r: raise ValueError(f"Ingrese otro valor. La matriz es de {self.r} filas")
        switch = 0
        elems = self.elems
        if self.by_row == False:
            elems = self.switch().elems
            switch = 1
        n_elems =  elems[:j*self.c - self.c] + elems[j*self.c:]
        if switch==1: self.switch()
        return Myarray(n_elems, self.r-1, self.c, self.by_row)
    
    def del_col(self, k, *args):
        """
        Se encarga de crear un nuevo objeto con la misma matriz pero sin la columna k
        
        Parameters
        Parameters
        ----------
        k : int
            Es la columna que se desa eliminar.

        Returns
        -------
        TYPE Myarray
            Es un objeto similar a elems pero sin la columna k y con c = c-1.
            .

        """
        if k<=0 or k > self.c: raise ValueError(f"Ingrese otro valor. La matriz es de {self.c} columnas")
        switch = 0
        elems = self.elems
        if self.by_row:
            elems = self.switch().elems
            switch = 1
        n_elems =elems[:k*self.r - self.r] + elems[k*self.r:]  
        if switch==1: 
            self.switch()
            salida = Myarray(n_elems, self.r, self.c-1, False).switch()
        else:
            salida = Myarray(n_elems, self.r, self.c-1, False)
        return salida
    
    def swap_rows(self, j, k, *args):
        """
        La funcion puede recibir listas ordenadas por filas o por columnas y devolvera otra con las filas
        intercambiadas pero con la misma manera de lectura de la lista. Si by_row = True, by_row seguira siendo
        True y viceversa.

        Parameters
        ----------
        j : Int
            Numero de fila que se desea intercambiar.
        k : int
            Numero de fila que se desea intercambiar.

        Returns
        -------
        TYPE Myarray
            Devuelve un objeto con una matriz identica pero con las filas j y k intercambiadas entre si.

        """
        if j <= 0 or j > self.r or k<=0 or k>self.r: print(f"Ingrese valores de filas validas. La matriz es de {self.r} filas")
        eelems = self.elems
        if self.by_row == False:
            for i in range(0, self.c):
                eelems[i*self.r+(j-1)], eelems[i*self.r+(k-1)] = self.elems[i*self.r+(k-1)], self.elems[i*self.r+(j-1)]
        else:
            fila_j, fila_k = eelems[(j-1)*self.c:(j)*self.c], eelems[(k-1)*self.c:(k)*self.c]
            eelems = eelems[:(j-1)*self.c] + fila_k + eelems[(j)*self.c:(k-1)*self.c] + fila_j + eelems[(k)*self.c:] 
        return Myarray(eelems, self.r, self.c, self.by_row)
    
    def swap_cols(self, l, m, *args):
        """
        La funcion puede recibir listas ordenadas por filas o por columnas y devolvera otra con las columnas
        intercambiadas pero con la misma manera de lectura de la lista. Si by_row = True, by_row seguira siendo
        True y viceversa.

        Parameters
        ----------
        l : Int
            Numero de columna que se desea intercambiar.
        m : int
            Numero de columna que se desea intercambiar.

        Returns
        -------
        TYPE Myarray
            Devuelve un objeto con una matriz identica pero con las columnas l y m intercambiadas entre si.

        """
        if l <= 0 or l > self.c or m <= 0 or m > self.c: print(f"Ingrese valores de columnas validas. La matriz es de {self.c} columnas")
        eelems = [i for i in self.elems]
        if self.by_row:
            for i in range(0,self.r):
                eelems[i*self.c+(l-1)], eelems[i*self.c+(m-1)] = eelems[i*self.c+(m-1)], eelems[i*self.c+(l)-1]
        else:
            columna_l, columna_m = eelems[(l-1)*self.r:(l)*self.r], eelems[(m-1)*self.r:(m)*self.r]
            eelems = eelems[:(l-1)*self.r] + columna_m + eelems[(l)*self.r:(m-1)*self.r] + columna_l + eelems[(m)*self.r:] 
        return Myarray(eelems, self.r, self.c, self.by_row)
    
    def scale_row(self, j, x, *args):
        """
        Este metodo multiplica todos los valores de la fila j por el escalar x. Devuelve un objeto identico 
        pero en la matriz, la fila j es j*x.
        Parameters
        ----------
        j : Int
            Numero de la fila que se desea multiplicar.
        x : int
            Valor por el que se desea multiplicar los elementos de la fila.

        Returns
        -------
        salida : Myarray
            Devuelve un objeto Myarray con la fila j multiplicada por el escalar x.

        """
        if j <= 0 or j > self.r: print(f"Ingrese una fila valida. La matriz tiene {self.r} filas")
        switch = 0
        if self.by_row == False:
            self.switch()
            switch = 1
        scale = []
        [scale.append(elemento * x) for elemento in self.elems[j*self.c - self.c : j*self.c]]
        n_elems =  self.elems[:j*self.c - self.c] + scale + self.elems[j*self.c:]
        if self.by_row == False:
            salida = Myarray(n_elems, self.r, self.c, self.by_row).switch()
        else:
            salida = Myarray(n_elems, self.r, self.c, self.by_row)
        if switch==1: self.switch()
        return salida
    
    def scale_col(self, k, y, *args):
        """
        Este metodo multiplica todos los valores de la columna k por el escalar x. Devuelve un objeto identico 
        pero en la matriz, la columna k es k*y.
        Parameters
        ----------
        k : int
            Numero de la columna que se desea multiplicar.
        y : int
            Valor por el que se desea multiplicar a los elementos de la columna k.

        Returns
        -------
        salida : Myarray
            Devuelve un objeto Myarray con la columna k multiplicada por el escalary.

        """
        if k <= 0 or k > self.c: print(f"Ingrese una fila columna. La matriz tiene {self.c} columnas")
        switch = 0
        if self.by_row:
            self.switch()
            switch = 1
        scale = []
        [scale.append(elemento * y) for elemento in self.elems[k*self.r - self.r : k*self.r]]
        n_elems = self.elems[:k*self.r - self.r] + scale +  self.elems[k*self.r:]  
        if self.by_row == False:
            salida = Myarray(n_elems, self.r, self.c, self.by_row)
        else:
            salida = Myarray(n_elems, self.r, self.c, self.by_row).switch()
        if switch==1: self.switch()
        return salida
    
    def transpose(self, *args):
        """
        Devuelve la transpuesta de una matriz. La matriz debe ser NxN.

        Returns
        -------
        TYPE Myarray
            Devuelve u objeto con la matriz traspuesta.

        """
        if self.r != self.c:raise ValueError(f"Para realizar la transpuesta la matriz debe ser de NxN, en este caso es {self.r}x{self.c}") 
        n_elems, f = [], 1
        if self.by_row:
            while f <= self.c:
                [n_elems.append(self.elems[elemento-1]) for elemento in range(f,len(self.elems)+1, self.c)]
                f += 1
        else:
            while f <= self.r:
                [n_elems.append(self.elems[elemento-1]) for elemento in range(f,len(self.elems)+1, self.r)]
                f += 1            
        return Myarray(n_elems, self.c, self.r, self.by_row)
    
    def flip_rows(self, *args):
        """
        Crea un nuevo objete que refeleje especularmente las filas de la matriz
        Returns
        -------
        TYPE Myarray
            Devuelve una copia del elemento de la clase, pero reflejado especularmente en sus columnas o fila.

        """
        n_elems = Myarray(self.elems, self.r, self.c, self.by_row)
        by_row = self.by_row
        if self.by_row:
            for i in range(1, self.r//2+1):
                n_elems = n_elems.swap_rows(i, self.r-i+1)
            self.by_row = by_row
        else:
            for i in range(1, self.c//2+1):
                self.by_row = True
                n_elems = n_elems.swap_cols(i, self.c-i+1)
        self.by_row=by_row
        return n_elems
    
    def flips_cols(self, *args):
        """
        Crea un nuevo objete que refeleje especularmente las columnas de la matriz
        Returns
        -------
        n_elems : Myarray
            Devuelve una copia del elemento de la clase, pero reflejado especularmente en sus columnas o fila.

        """
        n_elems = Myarray(self.elems, self.r, self.c, self.by_row)
        aux = []
        by_row = self.by_row
        if self.by_row == False:
            for i in range(1, self.r//2+1):
                n_elems = n_elems.swap_cols(i, self.r+1-i)
        else:
            self.by_row = False
            for i in range (1, self.c//2+1):
                n_elems = n_elems.swap_cols(i, self.c+1-i)
        self.by_row=by_row
        print(by_row, self.by_row)
        return Myarray(n_elems.elems, self.r, self.c, by_row)
    
    def pass_rows(self, l, direc, *args):
        """
        Recibe en que dirrecion se deben mover las filas. Este metodo es utilizado para shift. 
        Parameters
        ----------
        l : int
            Cantidad de lugares que se desea mover la fila.
        direc : str
            Direccion a la que se quieren mover las filas.


        Returns
        -------
        n_elems : list
            Devuelve una lista con la matriz con filas combiadas.

        """
        if l > self.r:
            l = l % self.r + 1
        n_elems, aux= [], self.elems
        if self.by_row == False:
            aux = self.switch().elems
        if direc[0].lower() == "u":
            filas = aux[(l)*self.c:]
            n_elems =  filas + aux[:(l)*self.c] 
        else:
            filas = aux[(self.r-l)*self.c:]
            n_elems =  aux[:(self.r-l)*self.c] + filas
        return n_elems
    
    def pass_cols(self, m, direc, *args):
        """
        Recibe en qeu direccion se deben mover las columnas. Este metodo es utilizado par shift
        Parameters
        ----------
        m : int
            Cantidad de lugares qeu se desea mover las columnas.
        direc : str
            Direccion a las que se desea mover las columnas .
            
        Returns
        -------
        n_elems : list
            Devuelve una lisata con la matriz con columnas cambiadas.

        """
        if m > self.c:
            m = m % self.c + 1
        n_elems = []
        aux = self.elems
        if self.by_row:
            aux = self.switch().elems
        if direc[0].lower() == "r":
            columnas = aux[(m)*self.r:]
            n_elems = columnas + aux[:(m)*self.r]
        else:
            columnas = aux[(self.c-m)*self.r:]
            n_elems =  columnas + aux[:(self.c-m)*self.r] 
            
        return n_elems

    def shift(self, d, c, *args):
        """
        Mueve las filas/columnas una cantidad c de lugares en la dirrecion d
        Parameters
        ----------
        d : str
            Direccion a la que se desea mover los elementos de la matriz.
        c : TYPE
            Cantidad de movimientos que deben hacer..
    
        Returns
        -------
        salida : Myarray
            Devuelve un objeto con la matriz modificada por los movimientos de filas y/o columnas.

        """
        if d[0].lower() not in "rlud": raise ValueError(f"{d} no es una direccion valida o {c} no es una cantidad valida, ingrese otra.")
        else:
            if d[0].lower() in "ud":
                if self.by_row: salida = Myarray(self.pass_rows(c, d[0]), self.r, self.c)
                else:salida = Myarray(self.pass_rows(c, d[0]), self.r, self.c).switch()
            else: 
                if self.by_row == False:salida = Myarray(self.pass_cols(c, d[0]), self.r, self.c, False)
                else:salida = Myarray(self.pass_cols(c, d[0]), self.r, self.c, False).switch()
        return salida
    
    def det(self, *args):
        aux = Myarray(self.elems, self.r, self.c, self.by_row)
        sub_matriz = Myarray(self.elems, self.r, self.c, self.by_row)
        dete = 0
        if self.r == 2:
            dete = aux.get_elem(1,1) * aux.get_elem(2,2) - aux.get_elem(1,2) * aux.get_elem(2,1)
        else:
            for i in range(0, self.r):
                n = aux.get_elem(1,i+1)
                sub_matriz = aux.del_col(i+1)
                sub_matriz = sub_matriz.del_row(1)
                dete += sub_matriz.det() * n * (-1) ** (i)
        return dete
    
    def myprint(self):
        print("\n")
        for k in range(1, self.r+1):
            print(self.get_row(k))
        print("\n")
        return None
#
    def summ(self, m1):
        """
        Suma dos matrices de iguales dimensiones y devolvera un objeto con la matriz de la suma. Mantendra el by_row
        de la matriz a la que se le aplica el metodo.
        Parameters
        ----------
        m1 : Myarray
            Es el objeto con la matriz que se sumara.
        Returns
        -------
        m3 : Myarray
            Es el objeto que contiene la suma de ambas matrices.
        """
        if self.by_row == m1.by_row:
            m3 =[e1 + e2 for e1, e2 in zip(m1.elems,self.elems)]
        elif self.by_row == False and m1.by_row:
            elems = self.switch().elems
            m3 =[e1 + e2 for e1, e2 in zip(m1.elems,elems)]
        else:
            m1 = m1.switch()
            m3 =[e1 + e2 for e1, e2 in zip(m1.elems,self.elems)]
        return Myarray(m3, m1.r, m2.c, self.by_row)
    
    def resm(self, m1):
        """
        Resta dos matrices de iguales dimensiones y devolvera un objeto con la matriz de la resta. Mantendra el by_row
        de la matriz a la que se le aplica el metodo.
        Parameters
        ----------
        m1 : Myarray
            Es el objeto con la matriz que se restara.
        Returns
        -------
        m3 : Myarray
            Es el objeto que contiene la resta de ambas matrices.
        """
        if self.by_row == m1.by_row:
            m3 =[e2 - e1 for e1, e2 in zip(m1.elems,self.elems)]
        elif self.by_row == False and m1.by_row:
            elems = self.switch().elems
            m3 =[e2 - e1 for e1, e2 in zip(m1.elems,elems)]
        else:
            m1 = m1.switch()
            m3 =[e2 - e1 for e1, e2 in zip(m1.elems,self.elems)]
        return Myarray(m3, m1.r, m2.c, self.by_row)
#
    def __add__(self, n):
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 + e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
        else: raise ValueError(f"El parametro de entrada no es valido, debe ser tipo int o Myarray")
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __radd__(self, n):
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 + e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
        else: print(f"El parametro de entrada no es valido, debe ser tipo int o Myarray")
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __sub__(self, n):
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 - e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 - e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 - e1 for e1, e2 in zip(n.elems,self.elems)]
        else: raise ValueError(f"El parametro de entrada no es valido, debe ser tipo int o Myarray")
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __rsub__(self, n):
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 - e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 - e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 - e1 for e1, e2 in zip(n.elems,self.elems)]
        else: print(f"El parametro de entrada no es valido, debe ser tipo int o Myarray")
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __radd__(self, n):
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 + e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
        else: print('El parametro de entrada no es valido, debe ser tipo int o Myarray')
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __mul__(self, n):
        return Myarray([n*elemento for elemento in self.elems], self.r, self.c, self.by_row) if (isinstance(n, float)) else print(f"El parametro de entrada no es valido, debe ser tipo int")
    
    def __rmul__(self, n):
        return Myarray([n*elemento for elemento in self.elems], self.r, self.c, self.by_row) if (isinstance(n, float)) else print(f"El parametro de entrada no es valido, debe ser tipo int")
        
    def __matmul__(self, n):
        if isinstance(n, type(self)) or self.c == n.r:
            elems = []
            for i in range(1, self.r + 1):
                for m in range(1, n.c+1):
                    elems.append(sum(map( lambda x: x[0] * x[1] , zip(self.get_row(i), n.get_col(m)))))
        return Myarray(elems, self.r, n.c, self.by_row)
        
    def __rmatmul__(self, n):
        if isinstance(n, type(self)) and self.c == n.r:
            elems = []
            for i in range(1, self.r + 1):
                for m in range(1, n.c+1):
                    elems.append(sum(map( lambda x: x[0] * x[1] , zip(self.get_row(i), n.get_col(m)))))
        return Myarray(elems, n.r, self.c, self.by_row)
    
    def __pow__(self, m):
        elems = self
        elems_copia = self
        if m == 1: elems.elems = 0
        else:
            for i in range(m-1):
                elems = elems @ elems_copia
        return elems
    
    def eye(self, r):
        #if self.r != self.c: raise ValueError(f"La matriz debe ser cuadrada")
        lista = []
        for i in range(0,r-1):
            lista += [1]+ r*[0]
        lista += [1]
        return Myarray(lista, r, r)
        
    def swap(self, n, m, row=True):
        if row == True: elems, x = self, self.r
        else: elems, x = self, self.c
        # z=max(self.c,self.r)
        iden = self.eye(x)
        index_n, index_m = iden.elems[(n-1)*x:n*x].index(1), iden.elems[(m-1)*x:m*x].index(1)
        iden.elems[index_n + (n-1) * x], iden.elems[index_m + (m-1) * x] = 0, 0
        iden.elems[index_m + (n-1) * x], iden.elems[index_n + (m-1) * x] = 1, 1
        return  Myarray(iden.elems, iden.r, iden.c, iden.by_row) @ elems if row==True else elems @ Myarray(iden.elems, iden.r, iden.c, self.by_row)
    
    # def del1(self, n, row=True):
    #     if self.by_row == True: elems = self
    #     else: elems = self.switch()
    #     iden = self.eye()
    #     index_n = iden[(n-1)*self.c : n*self.c].index(1)
    #     iden[index_n] = 0
    #     return  Myarray(iden, self.r, self.c, self.by_row) @ elems if row==True else elems @ Myarray(iden, self.r, self.c, self.by_row)
    
    def del_col1(self, n):#tengo que eliminar la columna n
        iden, e = self.eye(self.c), []
        for i in range(iden.r):
            fila = iden.elems[i*self.c:(i+1)*self.c]
            e += fila[:n-1] + fila[n:] 
        print(e)
        iden.elems, iden.c = e, iden.c-1
        return self @ iden
    
    def del_row1(self, n):#tengo que eliminar la columna n
        iden, e = self.eye(self.r), []
        for i in range(iden.r):
            fila = iden.elems[i*self.r:(i+1)*self.r]
            e += fila[:n-1] + fila[n:] 
        iden.elems, iden.r = e, iden.r-1
        return iden @ self
    
    def m_cofactor(self, *args):
        aux = self
        sub_matriz = self
        dete = []
        if self.r == 2:
            dete = aux.get_elem(1,1) * aux.get_elem(2,2) - aux.get_elem(1,2) * aux.get_elem(2,1)
        else:
            for e in range(self.r):
                for i in range(self.r):
                    sub_matriz = aux
                    sub_matriz = sub_matriz.del_col(i+1)
                    sub_matriz = sub_matriz.del_row(1)
                    dete.append(sub_matriz.det() * (-1) ** (e))
                aux = aux.shift("u", 1)
        return Myarray(dete, self.r, self.c, self.by_row)
    
    def inversa(self):
        matriz_cofactor = self.m_cofactor().transpose()
        detA = 1/self.det()
        return detA * matriz_cofactor
    
m1 =Myarray([1,0,
             0,0,
             0,1], 2,3)

m2 =Myarray([1,2,3,5,
              4,5,6,5,
              7,8,95,5,
              10,11,12,500],4,4)
#a2 = m.inversa()
i.myprint()

#%%
if __name__ == "__main__":
    
    matriz = Myarray([1,2,3,5,
                  4,5,6,5,
                  7,8,95,5,
                  10,11,12,500],4,4)
    
    #Atributos
    print(matriz.elems)
    print(matriz.r)#Cantidad de filas
    print(matriz.c)#Cantidad de columnas
    print("-----------------------------")
    print(matriz.by_row)

    #Get_pos
    print(matriz.get_pos(3,1))
    #print(matriz.get_pos(5,5))#Las cordenadas no eexiste
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Get_row
    print(matriz.get_row(2))
    #print(matriz.get_row(5))#No existe la fila 5
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Get_col
    print(matriz.get_col(2))
    #print(matriz.get_col(5))#No existe la columna 5
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Get_elem
    print(matriz.get_elem(3,3))
    #print(matriz.get_elem(1,6))#No esxite la columna 6
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #del_row
    matriz_2 = matriz.del_row(2)
    matriz_2.myprint()
    #matriz_2 = matriz.del_row(5)#Tira error porque no exixte la fila 5
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #del_col
    matriz_3 = matriz.del_col(3)
    matriz_3.myprint()
    #matriz_3 = matriz.del_col(8)#Tira error, no existe la columna 8
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Swaps_rows
    matriz_4 = matriz.swap_rows(2, 3)
    matriz.myprint()
    print("---")
    matriz_4.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Swap_cols
    matriz_5 = matriz.swap_cols(2, 3)
    matriz.myprint()
    print("---")
    matriz_5.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Scale_rows
    matriz_6 = matriz.scale_row(3,2)
    matriz.myprint()
    print("---")
    matriz_6.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Scale_cols
    matriz_7 = matriz.scale_col(3,2)
    matriz.myprint()
    print("---")
    matriz_7.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Transpoce
    matriz_8 = matriz.transpose()
    matriz.myprint()
    print("---")
    matriz_8.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Flip_rows
    matriz_9 = matriz.flip_rows()
    matriz.myprint()
    print("---")
    matriz_9.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Flips_rows
    matriz_10 = matriz.flips_cols()
    matriz.myprint()
    print("---")
    matriz_10.myprint()
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #det
    determinante = matriz.det()
    print(matriz.elems)
    matriz.myprint()
    print("---")
    print(f"El determinante es {determinante}")
    print("-----------------------------")
    print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #Shift
    matriz_11 = matriz.shift("u", 1)
    matriz.myprint()
    print("---")
    matriz_11.myprint()
    print("-----------------------------")
