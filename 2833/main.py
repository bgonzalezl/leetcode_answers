class Solution:
    """
    Esta clase Solution con el método furthestDistanceFromOrigin resuelve el problema '2833. Furthest Point From Origin' de Leetcode.

    Problema:
        You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.
        In the ith move, you can choose one of the following directions:
        - move to the left if moves[i] = 'L' or moves[i] = '_'
        - move to the right if moves[i] = 'R' or moves[i] = '_'
        Return the distance from the origin of the furthest point you can get to after n moves.
    
    Comentarios:
        El método count() de la clase string es la que permite que la solución sea tan rápida y fácil de entender, ya que devuelve un número entero, cuyo
        valor es las veces que aparece un caracter o letra en el propio string. 
        En cuando a las cuentas de los pasos, se menciona en el problema que el símbolo "_" puede ir a la izquiera o a la derecha, y en los ejemplos de
        ejecución los strings pasan de "L_RL__R" a "LLRLLLR" o "_R__LL_" a "LRLLLLL". Con esto se puede ver que el elemento más presente (Ya sea L o R)
        es el que define por cuál se deben de reemplazar los _. Con esto en mente, la cuenta final se termina definiendo como la suma de el elemento más 
        numeroso y los espacios menos la suma de el elemento restante.

    Acercamiento:
        1. Se cuentan las ocurrencias de L, R y _ por separado.

        2. Se comparan las ocurrencias de L y R, y dependiendo de cuál sea la más grande, se realiza la resta añadiendo las ocurrencias de _.

        3. En caso de que el string esté compuesto solamente de _, la cantidad de movimientos es la cantidad de ocurrencias de _.
    """
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r_count = moves.count("R")
        l_count = moves.count("L")
        leap_count = moves.count("_")
        if (r_count >= l_count) or (r_count == 0 and l_count == 0):
            return abs((r_count + leap_count) - l_count)
        else:
            return abs(r_count - (l_count + leap_count))
#Runtime: 0ms (Beats 100%)
#Memoria: 19.17MB (Beats 88.69%)
