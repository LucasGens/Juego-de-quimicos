# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 02:21:32 2023

@author: lucas
"""


# %%
class Myarray:
    def __init__(self, elems, r, c, by_row=True):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        if self.r * self.c != len(self.elems):
            raise ValueError("La cantidad de elementos no es correcta")

    def get_pos(self, k, j, *args):
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
        if k <= 0 or k > self.r or j <= 0 or j > self.c:
            raise ValueError(
                f"Las cordenadas no estan dentro del rango de la matriz. La matriz es {self.r}x{self.c}"
            )
        r, c = self.r, self.c
        if self.by_row:
            salida = k * c - (c - j)
        else:
            salida = j * r - (r - k)
        return salida

    def get_coords(self, m, *args):
        if m <= 0 or m > len(self.elems):
            raise ValueError(f"El elemento n {m} no existe)")
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
        columna_numero = 0  # esta es la columna , pero al comenzar con indice 0, al comienzo toma valor 0
        if self.by_row == False:
            e = self.r
            by_row = True
        else:
            e = self.c
            by_row = False
        while (
            columna_numero < e
        ):  # cada vez que pasa por el ciclo se mueve una columna a la derecha para agarrar sus elementos
            [n_elems.append(elemento) for elemento in (self.elems[columna_numero::e])]
            columna_numero += 1
        # self.elems = n_elems le mandaba esto como parametro
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
        if j <= 0 or j > self.c:
            raise ValueError(f"Ingrese otro valor. La matriz es de {self.c} columnas")
        salida = []
        switch = 0
        if self.by_row:
            salida = self.elems[j - 1 :: self.c]
            switch = 1
        else:
            for i in range(j - 1, len(self.elems), self.c):
                salida.append(self.elems[i])
        if switch == 1:
            self.switch()
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
        if k <= 0 or k > self.r:
            raise ValueError(f"Ingrese otro valor. La matriz es de {self.r} filas")
        switch = 0
        if self.by_row == False:
            self = self.switch()
            switch = 1
        salida = self.elems[(k - 1) * self.c : k * self.c]
        self.switch()
        if switch == 1:
            self = self.switch()
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
        if k <= 0 or k > self.c or j < 0 or j > self.r:
            raise ValueError(
                f"Las cordenasa no estan dentro del rango de la matriz. La matriz es {self.r}x{self.c}"
            )
        switch = 0
        indice = ((j - 1) * self.c + k) - 1
        if self.by_row == False:
            self.switch()
            switch = 1
            indice = (j - 1) * self.r
        salida = self.elems[indice]
        if switch == 1:
            self.switch()
        return salida

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
        if j <= 0 or j > self.r:
            raise ValueError(f"Ingrese otro valor. La matriz es de {self.r} filas")
        switch = 0
        elems = self.elems
        if self.by_row == False:
            elems = self.switch().elems
            switch = 1
        n_elems = elems[: j * self.c - self.c] + elems[j * self.c :]
        return Myarray(n_elems, self.r - 1, self.c).switch() if switch == 1 else Myarray(n_elems, self.r - 1, self.c)

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
        if k <= 0 or k > self.c:
            raise ValueError(f"Ingrese otro valor. La matriz es de {self.c} columnas")
        switch = 0
        elems = self.elems
        if self.by_row:
            elems = self.switch().elems
            switch = 1
        n_elems = elems[: k * self.r - self.r] + elems[k * self.r :]
        return Myarray(n_elems, self.r, self.c - 1, False).switch() if switch == 1 else Myarray(n_elems, self.r, self.c - 1, True)

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
        if j <= 0 or j > self.r or k <= 0 or k > self.r:
            print(f"Ingrese valores de filas validas. La matriz es de {self.r} filas")
        eelems = self.elems
        if self.by_row == False:
            for i in range(0, self.c):
                eelems[i * self.r + (j - 1)], eelems[i * self.r + (k - 1)] = (
                    self.elems[i * self.r + (k - 1)],
                    self.elems[i * self.r + (j - 1)],
                )
        else:
            fila_j, fila_k = (
                eelems[(j - 1) * self.c : (j) * self.c],
                eelems[(k - 1) * self.c : (k) * self.c],
            )
            eelems = (
                eelems[: (j - 1) * self.c]
                + fila_k
                + eelems[(j) * self.c : (k - 1) * self.c]
                + fila_j
                + eelems[(k) * self.c :]
            )
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
        if l <= 0 or l > self.c or m <= 0 or m > self.c:
            print(
                f"Ingrese valores de columnas validas. La matriz es de {self.c} columnas"
            )
        eelems = [i for i in self.elems]
        if self.by_row:
            for i in range(0, self.r):
                eelems[i * self.c + (l - 1)], eelems[i * self.c + (m - 1)] = (
                    eelems[i * self.c + (m - 1)],
                    eelems[i * self.c + (l) - 1],
                )
        else:
            columna_l, columna_m = (
                eelems[(l - 1) * self.r : (l) * self.r],
                eelems[(m - 1) * self.r : (m) * self.r],
            )
            eelems = (
                eelems[: (l - 1) * self.r]
                + columna_m
                + eelems[(l) * self.r : (m - 1) * self.r]
                + columna_l
                + eelems[(m) * self.r :]
            )
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
        if j <= 0 or j > self.r:
            print(f"Ingrese una fila valida. La matriz tiene {self.r} filas")
        switch = 0
        if self.by_row == False:
            n_elems = self.switch().elems
            switch = 1
        else:
            n_elems = self.switch().elems
        scale = []
        [
            scale.append(elemento * x)
            for elemento in n_elems[j * self.c - self.c : j * self.c]
        ]
        nn_elems = n_elems[: j * self.c - self.c] + scale + n_elems[j * self.c :]
        if self.by_row == False:
            salida = Myarray(nn_elems, self.r, self.c, True).switch()
        else:
            salida = Myarray(nn_elems, self.r, self.c, self.by_row)
        if switch == 1:
            self.switch()
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
        if k <= 0 or k > self.c:
            print(f"Ingrese una fila columna. La matriz tiene {self.c} columnas")
        switch = 0
        if self.by_row:
            # TODO Guarda el switch ahi no esta haciendo nada si no lo asignas a una nueva variable
            nn_elems = self.switch().elems
            switch = 1
        else:
            nn_elems = self.elems
        scale = []
        # TODO no hagas list comp si no vas a asignarlo a nada.
        [
            scale.append(elemento * y)
            for elemento in nn_elems[k * self.r - self.r : k * self.r]
        ]
        n_elems = nn_elems[: k * self.r - self.r] + scale + nn_elems[k * self.r :]

        if switch == 1:
            salida = Myarray(n_elems, self.r, self.c, self.by_row).switch()
        else:
            salida = Myarray(n_elems, self.r, self.c, self.by_row)
        return salida

    def transpose(self, *args):
        """
        Devuelve la transpuesta de una matriz. La matriz debe ser NxN.

        Returns
        -------
        TYPE Myarray
            Devuelve u objeto con la matriz traspuesta.

        """
        # if self.r != self.c:raise ValueError(f"Para realizar la transpuesta la matriz debe ser de NxN, en este caso es {self.r}x{self.c}")
        n_elems, f = [], 1
        if self.by_row:
            while f <= self.c:
                [
                    n_elems.append(self.elems[elemento - 1])
                    for elemento in range(f, len(self.elems) + 1, self.c)
                ]
                f += 1
        else:
            while f <= self.r:
                [
                    n_elems.append(self.elems[elemento - 1])
                    for elemento in range(f, len(self.elems) + 1, self.r)
                ]
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
            for i in range(1, self.r // 2 + 1):
                n_elems = n_elems.swap_rows(i, self.r - i + 1)
            self.by_row = by_row
        else:
            for i in range(1, self.c // 2 + 1):
                self.by_row = True
                n_elems = n_elems.swap_cols(i, self.c - i + 1)
        self.by_row = by_row
        return n_elems

    def flip_cols(self, *args):
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
            for i in range(1, self.r // 2 + 1):
                n_elems = n_elems.swap_cols(i, self.r + 1 - i)
        else:
            self.by_row = False
            for i in range(1, self.c // 2 + 1):
                n_elems = n_elems.swap_cols(i, self.c + 1 - i)
        self.by_row = by_row
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
        n_elems, aux = [], self.elems
        if self.by_row == False:
            aux = self.switch().elems
        if direc[0].lower() == "u":
            filas = aux[(l) * self.c :]
            n_elems = filas + aux[: (l) * self.c]
        else:
            filas = aux[(self.r - l) * self.c :]
            n_elems = aux[: (self.r - l) * self.c] + filas
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
            columnas = aux[(m) * self.r :]
            n_elems = columnas + aux[: (m) * self.r]
        else:
            columnas = aux[(self.c - m) * self.r :]
            n_elems = columnas + aux[: (self.c - m) * self.r]

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
        if d[0].lower() not in "rlud":
            raise ValueError(
                f"{d} no es una direccion valida o {c} no es una cantidad valida, ingrese otra."
            )
        else:
            if d[0].lower() in "du":
                if self.by_row:
                    salida = Myarray(self.pass_rows(c, d[0]), self.r, self.c)
                else:
                    salida = Myarray(self.pass_rows(c, d[0]), self.r, self.c).switch()
                print(salida.elems)
            else:
                if self.by_row == False:
                    salida = Myarray(self.pass_cols(c[0], d[0]), self.r, self.c, False)
                else:
                    salida = Myarray(
                        self.pass_cols(c, d[0]), self.r, self.c, False
                    ).switch()
        return salida

    def det(self, *args):
        if self.by_row != True: aux, sub_matriz = self.switch(), self.switch()
        else: aux, sub_matriz = self, self
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
        for k in range(1, self.r + 1):
            print(self.get_row(k))
        print("\n")
        return None

    def __add__(self, n):
        """
        Realiza la suma de dos elementos. Pueden ser de clase Myarray o int.
        El objeto de typo Myarray se debe ubicar a la izquierda. En caso de ser 
        un int, este valor sera sumado a cada elemento de la matriz.

        Parameters
        ----------
        n : Int o Myarray
        OBjeto que sera sumado a self.

        Returns
        -------
        TYPE Myarray
        Suma de los dos valres.

        """
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
        
        """
        Realiza la suma de dos elementos. Pueden ser de clase Myarray, int o float.
        El objeto de typo Myarray se debe ubicar a la derecha. En caso de ser int se
        sumara a cada elemento de la matriz.

        Parameters
        ----------
        n : Int o Myarray
        Objeto al que se le sumara self.

        Returns
        -------
        TYPE Myarray
        Suma de los dos valores.

        """
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 + e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 + e1 for e1, e2 in zip(n.elems,self.elems)]
        else: raise ValueError ("El parametro de entrada no es valido, debe ser tipo int o Myarray")
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __sub__(self, n):
        """
        Permite mediante el operador algebraico "-" realizar la resta de dos matrices o de 
        int a un matriz definida. El objeto de tipo Myarray debe ser ubicado a la izquierda.

        Parameters
        ----------
        n : Int o Myarray
        Objeto que sera sumando a self.

        Returns
        -------
        TYPE Myarray
            Objeto de tipo Myarray que sera proveniente de la suma de self y n.

        """
        if (isinstance(n, int)): salida = [n+elemento for elemento in self.elems]
        elif (isinstance(n, type(self))):
            if self.by_row == n.by_row: salida =[e2 - e1 for e1, e2 in zip(n.elems,self.elems)]
            elif self.by_row == False and n.by_row:
                elems = self.switch().elems
                salida =[e2 - e1 for e1, e2 in zip(n.elems,elems)]
            else:
                n = n.switch()
                salida =[e2 - e1 for e1, e2 in zip(n.elems,self.elems)]
        else: raise ValueError("El parametro de entrada no es valido, debe ser tipo int o Myarray")
        return Myarray(salida, self.r, self.c, self.by_row)
    
    def __rsub__(self, n):
        """
        Permite mediante el operador algebraico "-" realizar la resta de dos matrices o de 
        int a un matriz definida. El objeto n debe ser ubicado a la izquierda.

        Parameters
        ----------
        n : Int o Myarray
        Objeto que sera sumando a self.

        Returns
        -------
        TYPE Myarray
            Objeto de tipo Myarray que sera proveniente de la suma de n y self.

        """
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
    
    def __mul__(self, n):
        """
        Multiplica al atributo elems de Myarray por el escalar n. El objeto de tipo
        Myarray debe estar ubicado a la izquierda.

        Parameters
        ----------
        n : INt
            Escalar por el que se multiplicara a self.elems.

        Returns
        -------
        TYPE Myarray
        Obheto de tipo Myarray que cntiene la matriz multiplicada por el escalar n.

        """
        return Myarray([round(n*elemento, 2) for elemento in self.elems], self.r, self.c, self.by_row) if (isinstance(n, int) or type(n) == float) else print(f"El parametro de entrada no es valido, debe ser tipo int")
    
    def __rmul__(self, n):
        """
        Multiplica al atributo elems de Myarray por el escalar n. El objeto de tipo
        Myarray debe estar ubicado a la derecha.

        Parameters
        ----------
        n : INt
            Matriz que sera multiplicada por el escalar.

        Returns
        -------
        TYPE Myarray
        Obheto de tipo Myarray que fue multiplicado por el escalar.

        """
        return Myarray([round(n*elemento,2) for elemento in self.elems], self.r, self.c, self.by_row) if (isinstance(n, int) or type(n) == float) else print(f"El parametro de entrada no es valido, debe ser tipo int")
        
    def __matmul__(self, n):
        """
        Multiplica dos matrices de tipo Myarray. 

        Parameters
        ----------
        n : Myarray
            Matriz que postmultiplicar.

        Returns
        -------
        TYPE Myarray
            Matriz proveniente de la multiplicacion self * n.

        """
        if isinstance(n, type(self)) and self.c == n.r:
            elems = []
            for n_f in range(1, self.r + 1):
                for n_c in range(1, n.c+1):
                    lista = zip(self.get_row(n_f), n.get_col(n_c))
                    elems.append(sum(map( lambda x: x[0] * x[1] , lista)))
        else: raise ValueError("Ambos objetos deben ser de tipo Myarray. Ademas, la matriz de la derecha debe tener la misma cantidad de filas que columnas de la izquierda.")
        return Myarray(elems, self.r, n.c, self.by_row)
        
   
    def __pow__(self, m):
        """
        Eleva la una matriz n veces.

        Parameters
        ----------
        m : Int
            Cantidad de veces que se elevara la matriz.

        Returns
        -------
        elems : Myarray
            Matriz elevada n veces.

        """
        if self.c != self.r: raise ValueError("Solo es posible hacer potencias de matrices cuadradas")
        elems = self
        elems_copia = self
        if m == 1: elems.elems = 0
        else:
            for i in range(m-1):
                elems = elems @ elems_copia
        return elems
    
    def eye(self, r):
        """
        Cre la identidad de una matriz.

        Parameters
        ----------
        r : int
            Tamañano de la matriz

        Returns
        -------
        TYPE Myarray
            Identidad de la matriz de tamanño nxn.

        """
        #if self.r != self.c: raise ValueError(f"La matriz debe ser cuadrada")
        lista = []
        for i in range(0,r-1):
            lista += [1]+ r*[0]
        lista += [1]
        return Myarray(lista, r, r)
        
    def swap_col1(self, n, m):
        """
        Funcion que intercambia las columnas n y m de una matriz.
        Parameters
        ----------
        n : Int
            Columna que sera intercambiada por m.
        m : Int
            Columna que sera intercambiado por n.

        Returns
        -------
        TYPE Myarray
            Matriz con las columnas n y m swapeadas.

        """
        if n > self.r or m > self.r : raise ValueError(f"La fila n o m no existen, la matiz tiene {self.r} filas")
        e = []
        if self.by_row: iden, k = self.eye(self.c), self.c
        else: iden, k = self.eye(self.r), self.r
        for i in range(k):
             fila = iden.elems[i*k:(i+1)*k]
             n_n, m_m = fila[n-1], fila[m-1]
             fila[m-1], fila[n-1] = n_n, m_m
             e.extend(fila)
        return self @  Myarray(e, iden.r, iden.c, iden.by_row) if self.by_row else Myarray(e, iden.r, iden.c, self.by_row) @ self.switch()
        
    def swap_row1(self, n, m):
        """
        Funcion que intercambia las filas n y m de una matriz.
        Parameters
        ----------
        n : Int
            Fila que sera intercambiada por m.
        m : Int
            Fila que sera intercambiado por n.

        Returns
        -------
        TYPE Myarray
            Matriz con las filas n y m swapeadas.

        """
        if n > self.r or m > self.r: raise ValueError(f"La fila n o m no existen, la matiz tiene {self.r} filas")
        e = []
        if self.by_row: iden, k = self.eye(self.r), self.r
        else: iden, k = self.eye(self.c), self.c
        for i in range(k):
             fila = iden.elems[i*k:(i+1)*k]
             n_n, m_m = fila[n-1], fila[m-1]
             fila[m-1], fila[n-1] = n_n, m_m
             e.extend(fila)
        return  Myarray(e, iden.r, iden.c, self.by_row) @ self if self.by_row else self.switch() @  Myarray(e, iden.r, iden.c, iden.by_row), Myarray(e, iden.r, iden.c, iden.by_row)
    
    def del_col1(self, n):#tengo que eliminar la columna n
        """
        Elimina la columna numero n de la matriz. En caso de que la columna a eliminar exceda
        al valor de self.c arrojara un error. La primer columna de la matriz es 1.

        Parameters
        ---------
        n : int
            numero de columna que se quiere eliminar.
        """
        if n>self.c: raise ValueError("El parametro n excede el numero de columnas de la matriz")
        if self.by_row:
            iden, e = self.eye(self.c), []
            for i in range(iden.r):
                fila = iden.elems[i*self.c:(i+1)*self.c]
                e += fila[:n-1] + fila[n:]
            iden.elems, iden.c = e, iden.c-1
            salida = self @ iden
        else:
            iden, e = self.eye(self.r), []
            iden.elems = iden.elems[:(n-1)*self.r] + iden.elems[n*self.r:]
            iden.r -= 1
            salida = iden @ self
        return salida
    
    def del_row1(self, n):
        """
        Elimina la fila numero n de la matriz. En caso de que la fila a eliminar exceda
        al valor de self.r arrojara un error. La primer fila de la matriz es 1.

        Parameters
        ---------
        n : int
            numero de fila que se quiere eliminar.
        """
        if n>self.r: raise ValueError("El parametro n excede el numero de filas de la matriz")
        if self.by_row:
            iden = self.eye(self.r)
            iden.elems =iden.elems[:(n-1)*self.r] + iden.elems[(n)*self.r:]
            iden.r -= 1#Esto si es True
            salida = iden @ self
        else:
            iden, e =self.eye(self.c), [] 
            for i in range(self.c):
                fila = iden.elems[i*self.c:(i+1)*self.c]
                e += fila[:n-1] + fila[n:]
            iden.elems = e
            iden.c -= 1
            salida = self @ iden
        return salida
    
    def m_cofactor(self, *args):
        """
        Genera la matriz cofactor de la matriz dada.

        Returns
        -------
        TYPE Myarray
            Objeto que contiene como atributo la matriz cofacotora.

        """
        if self.r != self.c: raise ValueError("La matriz debe ser cuadrada")
        if self.by_row != True: aux, sub_matriz = self.switch(), self.switch()
        else: aux, sub_matriz = self, self
        dete = []
        if self.r == 2:
            dete = aux.get_elem(1,1) * aux.get_elem(2,2) - aux.get_elem(1,2) * aux.get_elem(2,1)
        else:
            for e in range(self.r):
                for i in range(self.r):
                    sub_matriz = aux
                    sub_matriz = sub_matriz.del_col(i+1)
                    sub_matriz = sub_matriz.del_row(1)
                    dete.append(sub_matriz.det() * (-1) ** (i-e))
                aux = aux.shift("u", 1)
        return Myarray(dete, self.r, self.c, self.by_row)
    
    def inversa(self):
        """
        Genera la inversa de una matriz. 

        Returns
        -------
        TYPE Myarray
            Es la matriz inversa de la matriz self.

        """
        if self.det() == 0: raise ValueError("La matriz no es inversible")
        matriz_cofactor = self.m_cofactor().transpose()
        detA = 1/self.det()
        return detA * matriz_cofactor
    
    def get_col1(self, n):
        if self.by_row: k = self.r
        else: k = self.c
        iden = k * [0]
        iden[n-1] = 1
        return self @  Myarray(iden, self.r, 1) if self.by_row else Myarray(iden, 1, self.r, False ) @ self
    
    def get_row1(self, n):
        if self.by_row: k = self.r
        else: k = self.c
        iden = k * [0]
        iden[n-1] = 1
        return Myarray(iden, 1, k) @ self if self.by_row else self @ Myarray(iden, k , 1, False)
    
    def get_elem1(self, r, c):
        columna = self.get_col1(c)
        elemento = columna.get_row1(r)
        return float(*elemento.elems)
        
    def b_inversa(self):
        """
        Calcula la inversa de una funcion mediante la multiplicacion  de las identidades
        utilizadas para convetir la matriz en una identidad

        Returns
        -------
        iden : Myarray
            Inversas de la matriz. Es un objeto de tipo Myarray.

        """
        matriz, iden = self, self.eye(self.r)
        for i in range(self.r):#Es indiferente a r, c, la matriz es cuadrada
            primeros = matriz.get_col1(i+1).elems#Lista con los primeros elementos de las columnas
            if primeros == (self.r-i) * [0] and len(primeros) > 1 : raise ValueError ("La matriz no es invercible")
            if matriz.get_elem1(i+1, i+1) == 0:
                for e in range(i,len(primeros)):#swapeo la fila con ceros
                    if matriz.get_elem1(i+1,i+1) == 0:
                        matriz, iden_s = matriz.swap_row1(i+1, e+1)
                        iden = iden_s @ iden
            
            iden_m = self.eye(self.r)# Multiplico por el escalar++
            iden_m.elems[iden_m.get_pos(i+1, i+1) - 1] = 1 / matriz.get_elem1(i+1, i+1)
            matriz, iden = iden_m @ matriz, iden_m @ iden
            
            for d in range(i+1, self.r):#Elimino los numeros de la columna de abajo
                iden_0= self.eye(self.r)
                if d == 0: continue
                else:
                    iden_0.elems[matriz.get_pos(d+1, i+1)-1] = -matriz.get_elem1(d+1, i+1)
                    matriz, iden = iden_0 @ matriz, iden_0 @ iden
                    
            for e in range(i):#Elimino los nuemroes de las columnas de arriba
                iden_1 = self.eye(self.r)
                iden_1.elems[iden_1.get_pos(e+1, i+1)-1] = -matriz.get_elem1(e+1, i+1)
                matriz, iden = iden_1 @ matriz, iden_1 @ iden
        return iden
    
                    
    def sol(self, rdo):
        """
        Calcula en conjunto solucion de un sistema lineal mediante la multiplicacion
        de la inversa y el resultdo.

        Parameters
        ----------
        rdo :   Myarray
            Resultado de las ecuacion del sistema.

        Returns
        -------
        TYPE Myarray
            Conjunto de solucion del sistema lineal.

        """
        return self.b_inversa() @ rdo

matriz_28 = Myarray([-27,9,-3,1,
                      -8,4,-2,1,
                      0,0,0,1,
                      -1,1,-1,1],4,4)

matriz_29 = Myarray([0,4,0,2],4,1)
pol = matriz_28.sol(matriz_29)
pol.myprint()
#Encontrar un polinomio que pase por los puntos (-3, 0), (-2, 4), (0, 0), (-1, 2)


# %%
if __name__ == "__main__":
    matriz = Myarray([1, 2, 3, 4, 5, 6], 2, 3)
    #matriz.switch().myprint()
    # print(matriz.elems)
    # print(matriz.r)  # Cantidad de filas
    # print(matriz.c)  # Cantidad de columnas
    # print("-----------------------------")
    # print(matriz.by_row)

    # # Get_pos
    # print(matriz.get_pos(3, 1))
    # # print(matriz.get_pos(5,5))#Las cordenadas no eexiste
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Get_row
    # print(matriz.get_row(2))
    # # print(matriz.get_row(5))#No existe la fila 5
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Get_col
    # print(matriz.get_col(2))
    # # print(matriz.get_col(5))#No existe la columna 5
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Get_elem
    # print(matriz.get_elem(3, 3))
    # # print(matriz.get_elem(1,6))#No esxite la columna 6
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # del_row
    # matriz_2 = matriz.del_row(2)
    # matriz_2.myprint()
    # # matriz_2 = matriz.del_row(5)#Tira error porque no exixte la fila 5
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # del_col
    # matriz_3 = matriz.del_col(3)
    # matriz_3.myprint()
    # # matriz_3 = matriz.del_col(8)#Tira error, no existe la columna 8
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Swaps_rows
    # matriz_4 = matriz.swap_rows(2, 3)
    # matriz.myprint()
    # print("---")
    # matriz_4.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Swap_cols
    # matriz_5 = matriz.swap_cols(2, 3)
    # matriz.myprint()
    # print("---")
    # matriz_5.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Scale_rows
    # matriz_6 = matriz.scale_row(3, 2)
    # matriz.myprint()
    # print("---")
    # matriz_6.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Scale_cols
    # matriz_7 = matriz.scale_col(3, 2)
    # matriz.myprint()
    # print("---")
    # matriz_7.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Transpoce
    # matriz_8 = matriz.transpose()
    # matriz.myprint()
    # print("---")
    # matriz_8.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Flip_rows
    # matriz_9 = matriz.flip_rows()
    # matriz.myprint()
    # print("---")
    # matriz_9.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Flips_rows
    # matriz_10 = matriz.flips_cols()
    # matriz.myprint()
    # print("---")
    # matriz_10.myprint()
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # det
    # determinante = matriz.det()
    # print(matriz.elems)
    # matriz.myprint()
    # print("---")
    # print(f"El determinante es {determinante}")
    # print("-----------------------------")
    # print(
    #     f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}"
    # )

    # # Shift
    # matriz_11 = matriz.shift("u", 1)
    # matriz.myprint()
    # print("---")
    # matriz_11.myprint()
    # print("-----------------------------")

    # add - radd
    # matriz_12 = matriz
    # matriz_13 = matriz_12 + matriz + matriz
    # matriz.myprint()
    # print("---")
    # matriz_13.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # # sub - rsub
    # matriz_14 = matriz
    # matriz_15 = matriz_12 - matriz - matriz
    # matriz.myprint()
    # print("---")
    # matriz_15.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # # mul - rmul
    # matriz_16 = 2 * matriz # matriz_16 * 2
    # matriz.myprint()
    # print("---")
    # matriz_16.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # # rmatmul
    # matriz_17 = Myarray([1,2,3,4,5,6], 3, 2)
    # matriz_18 = Myarray([1,2,3,4,5,6,7,8], 2, 4)
    # matriz_19 = matriz_17 @ matriz_18
    # print("---")
    # matriz_19.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # # Pow
    # matriz = Myarray([1,2,3,4,5,6,7,8,9], 3, 3)
    # matriz_20 = matriz ** 2
    # matriz.myprint()
    # print("---")
    # matriz_20.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # # Del_col1
    # matriz_22 = matriz.del_col1(1)#Agarra la matriz que cree en Pow  (Matriz linea 1173)
    # matriz.myprint()
    # print("---")
    # matriz_22.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # # Del_row1
    # matriz_23 = matriz.del_row1(1)#Agarra la matriz que cree en Pow  (Matriz linea 1173)
    # matriz.myprint()
    # print("---")
    # matriz_23.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # #swap_row1
    # matriz_24 = matriz.swap_row1(1, 3)#Agarra la matriz que cree en Pow  (Matriz linea 1173)
    # matriz.myprint()
    # print("---")
    # matriz_24.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # #swap_col1
    # matriz_25 = matriz.swap_col1(1, 3)#Agarra la matriz que cree en Pow  (Matriz linea 1173)
    # matriz.myprint()
    # print("---")
    # matriz_25.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    # #m_cofactor
    # matriz_26 = matriz.m_cofactor() #Agarra la matriz que cree en Pow  (Matriz linea 1173)
    # matriz.myprint()
    # print("---")
    # matriz_26.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    #inversa
    # matriz = Myarray([-27,9,-3,1,
    #                       -8,4,-2,1,
    #                       0,0,0,1,
    #                       -1,1,-1,1],4,4)
    # matriz_27 = matriz.inversa() #Agarra la matriz que cree en Pow  (Matriz linea 1173)
    # matriz.myprint()
    # print("---")
    # matriz_27.myprint()
    # print("-----------------------------")
    # print(f"la lista es {matriz.elems} las dimensiones son {matriz.r} x {matriz.c}. Esta ordenda por filas ? {matriz.by_row}")
    
    matriz_28 = Myarray([-27,9,-3,1,
                          -8,4,-2,1,
                          0,0,0,1,
                          -1,1,-1,1],4,4)
    
    matriz_29 = Myarray([0,4,0,4],4,1)
    (matriz_28.b_inversa()@matriz_29).myprint()