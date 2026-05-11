class Solution:
    """
    Esta clase Solution con el método separateDigits resuelve el problema '2553. Separate the digits in an Array' de leetcode.

    Problema:
        Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
        To separate the digits of an integer is to get all the digits it has in the same order.

    Comentarios:
        Lo que permite que esta solución ocupe poca memoria usando la división de los números como strings (que a diferencia del acercamiento que divide en decimales
        y los añade uno a uno, ocupa un poco más de memoria) es que se evita realizar operaciones redundantes o repetitivas (como primero pasar a una variable cada número convertido
        a string para luego usarlo) y que la lista original se limpia antes de devolver la nueva.

    Acercamiento:
        1. Se genera un nuevo arreglo para almacenar los números.

        2. Se transforma un número del arreglo 'nums' a String y cada caracter por separado se añade al nuevo arreglo.

        3. Se limpia 'nums' y se devuelve la lista con los números separados.
    """
    def separateDigits(self, nums: List[int]) -> List[int]:
        new_nums = []
        for element in nums:
            for l in str(element):
                new_nums.append(int(l))
        nums.clear()
        return new_nums
#Runtime: 3ms (Beats 76.03%)
#Memoria: 19.19MB (Beats 99.79%)
