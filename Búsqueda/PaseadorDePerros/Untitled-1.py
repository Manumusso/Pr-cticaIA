
ARBOL = (0,2),(1,0),(3,1),(3,4),(4,2)
TERO = (2,2)
RAMA = (1,1)
CANCHA = (3,3)
ENTRADA = (0,4)

DE_INTERES = (ARBOL,(RAMA,CANCHA))

ESTADO_INICIAL = (ENTRADA,DE_INTERES)

def en_grilla(posición):
    return all(0<=c<=4 for c in posición)

class ProblemPerros(SearchProblem):
    def isGoal(self,state):
        posicion_perro, por_visitar: state

        return len(por_visitar) == 0
    
    def Actions(self, state):
        posicion_perro, por_visitar: state
        available_actions = []
        posiciones_visitadas = DE_INTERES - por_visitar

        posibles_movimientos = []
        for f in posibles_movimientos[(1,0),(-1,0),(0,1),(0,-1)]:
            nueva_fila = posicion_perro[0]+f[0]
            nueva_columna = posicion_perro[1]+f[1]
            nueva_posicion = (nueva_fila,nueva_columna)

            if en_grilla(nueva_posicion) and nueva_posicion!= TERO and nueva_posicion not in posiciones_visitadas:
                available_actions.append(nueva_posicion)

        return available_actions
    def Results(self, state,action):
        posicion_perro, por_visitar: state
        nueva_posicion = action
        posicion_perro = nueva_posicion
        lactualizadaporvisitar = []

        for x in por_visitar.items():
            if x != nueva_posicion:
                lactualizadaporvisitar.append(x)
                ##Faltaría ver lo de la rama

        return (posicion_perro,lactualizadaporvisitar)

    def cost(self,state1,action,state2):
        nueva_posicion = action
        if nueva_posicion in ARBOL:
            return 20
        else:
            if nueva_posicion in RAMA:
                return 60
            else:
                if nueva_posicion in CANCHA:
                    return 120
                else:
                    return 10
    
    def heuristic(self,state):
        #Según el estado que estoy parado, 10 segundos por cada actividad que me falta pasar sin contar la que estoy parado.
        posicion_perro, por_visitar: state
        costo_heuristic = 0
        for x in por_visitar:
            if x != posicion_perro:
                costo_heuristic += 10
