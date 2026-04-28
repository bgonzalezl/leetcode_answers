class Solution:
    """
    Esta clase Solution con el método minOperations resuelve el problema '2033. Minimum Operations to Make a Uni-Value Grid' de Leetcode.

    Problema:
        You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
        A uni-value grid is a grid where all the elements of it are equal.
        Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

    Comentarios:
        La clave principal para entender la solución del problema es ver que el módulo de todos los valores y x de las listas aceptadas y con respuesta
        es de 0, a diferencia de las listas no aceptadas, ya que estas suelen tener al menos uno con valor diferente 
            Por ejemplo, para los valores de la lista [[1,2],[3,4]] y X = 2, sus módulos con 2 son 0, a excepción de 3. Esto hace imposible que los valores
            se puedan igualar usando saltos de 2 en 2.

    Acercamiento:
        1. Se aplana la lista dada "grid" con los valores para facilitar operaciones futuras y evitar tener que usar dos for anidados para acceder a
        los números.

        2. Se limpia la lista original, ya que no se seguirá utilizando en las operaciones siguientes y solo vuelve el programa más pesadfo en memoria.

        3. Se ordena la nueva lista aplanada y se obtiene la media como valor objetivo ya que es el que reduce al mínimo la cantidad de operaciones 
        a realizar. Por ejemplo, en una lista [1,2,3,4,5] y X = 1, el valor que reduce las operaciones al mínimo es el 3, ya que solo se necesitaría sumar:
        +2, +1, 0, -1 y -2, lo que nos da 6 operaciones en total, a diferencia de 2 o 4 que requieren 7 operaciones, o 1 y 5 que requieren de 10.

        4. Se verifica que cada elemento de la lista comparta el mismo resultante del módulo x, ya que eso quiere decir que los elementos pueden 
        sumarse o restarse por x hasta llegar al valor objetivo.

        5. Se suman la cantidad de operaciones (sumas o restas) necesarias para igualar cada elemento a la media
    
    Complejidad:
        En tiempo, O(n log n) por el ordenamiento.
        En espacio, O(n) por el aplanado del arreglo.

    La optimización principal del programa es la limpieza de grid y de pettan después de ser utilizadas, lo que reduce mucho el uso de memoria.
    """
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        moves = 0
        pettan = [item for sublist in grid for item in sublist]
        grid.clear()
        pettan.sort()
        pos_median = int(len(pettan)/2)
        if len(pettan)%2 == 0:
            median = pettan[pos_median-1]
        else:
            median = pettan[pos_median]
        for element in pettan:
            if element%x != pettan[0]%x:
                return -1
            if median > element:
                moves += (median - element)//x
            elif element > median:
                moves += (element - median)//x
        pettan.clear()
        return moves
#Runtime: 176ms (Beats 46.58%)
#Memoria: 37.4MB (Beats 100%)
