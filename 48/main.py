class Solution:
    """
    Esta clase Solution con el método rotate resuelve el problema '48. Rotate Image' de Leetcode.

    Problema:
        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.

    Comentarios:
        La idea de esta solución es aprovechar que el resultado de la transposición de la matriz (reemplazar el valor en [i][j] por [j][i])
        es idéntica a rotar 90 grados en sentido de las manecillas del reloj y luego invertir los números de cada fila. Por ende, se realiza
        la transposición (usando una doble asignación de valores para no depender de variables terciarias) seguida d euna inversión usando
        la operación [::-1]. (Se puede hacer de igual manera con el iterador list(Reversed(matrix[i])), pero durante la ejecución
        se usó más memoria).

    Acercamiento:
        1. Se obtiene la transpuesta de la matriz iterando con un valor dinámico que se salta la diagonal de la matriz y los valores a la izquierda
        ya que de hacerlo por toda la matriz se repetirían los valores y la matriz quedaría como empezó.

        2. Iterando por cada fila, se revierte el orden de los elementos con la operación [::-1].
    """
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
#Runtime: 0ms (Beats 100%)
#Memory: 19.14MB (Beats 92.56%)
