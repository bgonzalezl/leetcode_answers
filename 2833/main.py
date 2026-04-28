class Solution:
    """
    El siguiente programa resuelve el problema "2833. Furthest Point From Origin"
    """
    #TODO: Añadir un docstring explicando el problema y lo que hice xd
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
