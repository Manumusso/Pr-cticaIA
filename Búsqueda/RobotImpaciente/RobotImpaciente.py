

ENTRADA = (0,0)
SALIDA = (5,5)
PAREDES = ((0,1),(1,1),(1,4),(2,3),(3,1),(3,2),(3,5),(4,0),(4,2),(4,4),(5,2),(5,3))
ESTADO_INICIAL = (ENTRADA, PAREDES)

def isGrilla(posicion):
    return all(0<=c<=4 for c in posicion)
def CalcularDistanciaManhattan(posicion):
    distancia_m = abs(posicion[0]- SALIDA) + abs (posicion[1] - SALIDA)
    return distancia_m


class ProblemRobot(SearchProblem):

    def isGoal(self,state):
        posicion, paredes = state
        return posicion == SALIDA
    
    def actions(self,state):
        posicion, paredes = state
        avalaible_actions = []
        posibles_posiciones = []
        for pos in posibles_posiciones[(1,0),(-1,0),(0,1),(0,-1)]:
            fila = pos[0]
            columna = pos[1]
            nuevaposicion= (fila,columna)
            if isGrilla(nuevaposicion):
                ##Si la nueva posición se encuentra en la grilla, consulto si esta en presencia de una pared.
                if nuevaposicion in PAREDES:
                    avalaible_actions.append('Romper',nuevaposicion)
                else:
                    avalaible_actions.append('IrSinViolencia',nuevaposicion)

        return avalaible_actions
    
    def results(self,state,action):
        posicion, lparedes = state
        tipo_accion, posicionn = action

        if tipo_accion == 'Romper':
            #Elimino la pared.
            lparedes.remove(posicionn)
            posicion = posicionn
        if tipo_accion == 'IrSinViolencia':
            posicion = posicionn
        return (posicion,lparedes)    
    def cost(self,state1,action,state2):
        tipo_accion, posicion = action
        if tipo_accion == 'Romper':
            return 20
        if tipo_accion == 'IrSinViolencia':
            return 10
        
    def heuristic(self,state):
        posicion, lparedes = state
        #La heuristica corresponde al calculo de Manhattan del consumo como mínimo sin paredes.
        Distancia = CalcularDistanciaManhattan(posicion)

        return Distancia * 10







