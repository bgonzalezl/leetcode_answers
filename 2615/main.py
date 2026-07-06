class Solution:
    """
    Esta clase Solution con el método distance resuelve el problema '2615. Sum of Distances' de Leetcode.

    Problema:
        You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] 
        is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
        Return the array arr.
    
    Comentarios:
        La generación de un diccionario usando la lista inicial permite buscar más fácilmente los elementos repetidos
        para la obtención de las distancias, ya que se evita buscar elemento por elemento dentro de la lista.

    Acercamiento:
        1. Se genera el arreglo respuesta y el diccionario de tipo "defaultdict" para poder rellenarlos más adelante.

        2. Se llena el diccionario al iterar por la lista, asignando como llave el número y como valor, sus repeticiones a lo largo de la lista original.

        3. Se suman las posiciones de cada número repetido y se itera por cada posición para calcular la distancia total de cada elemento, usando la fórmula:
            arr[i] = total - (2 * left_sum) + v * (2 * i - m)
        
        4. Se regresa el arreglo obtenido.
    """
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        mp = defaultdict(list)

        for i, v in enumerate(nums):
            mp[v].append(i)

        for pos in mp.values():
            total = sum(pos)
            left_sum = 0
            m = len(pos)
            for i, v in enumerate(pos):
                ans[v] = total - (2 * left_sum) + v * (2 * i - m)
                left_sum += v
        return ans
#Memoria: 55.10MB (Beats 58.46%)
#Runtime: 127ms (Beats 58.68%)
