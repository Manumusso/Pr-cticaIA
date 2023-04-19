#Problema robot defensivos secretos

CENTRO_INVESTIGACION = (0,1)
BLOQUEOS = [(0,2),(1,3),(2,1)]
ROBOTS = [(0,1),(0,1)]

HayEmergencia = True
ESTADO_INICIAL = (ROBOTS,HayEmergencia)
POSICIONES_DEFENSIVAS = [(3,2),(0,4)]



def enGrilla(posicion):
    fila, columna = posicion
    return fila <= 0 and fila <= 3 and columna <= 0 and columna <= 4
        
def RetornarAdyacentes(posicion):
    Adyacentes = []
    posibles_movimientos = []
    fila,columna = posicion
    for movx,movy in posibles_movimientos[(0,1),(0,-1),(1,0),(-1,0)]:

        nueva_fila = movx + fila
        nueva_columna = movy + columna
        nueva_posicion = (nueva_fila, nueva_columna)

        if enGrilla(nueva_posicion) and nueva_posicion not in BLOQUEOS:
            Adyacentes.append(nueva_posicion)

    return Adyacentes
class RobotDefensivos(SearchProblem):
    
    def isGoal(self,state):
        #Entiendo que ubicarse en posiciones defensivas serian las entradas marcadas con flechas en el grafico del enunciado.
        posicion_robots, posEmergencia: state

        return (posicion_robots[0],posicion_robots[1]) in POSICIONES_DEFENSIVAS

    def Actions(self,state):
        posicion_robots, Emergencia: state
        avalaible_actions = []
        if Emergencia:
            #Robot1
            
            for posicion in RetornarAdyacentes(posicion_robots[0]):
                avalaible_actions.append('DefenderConR1',posicion)
            #Robot2
            for posicion in RetornarAdyacentes(posicion_robots[1]):
                avalaible_actions.append('DefenderConR2',posicion)
        else:
            #Cuando no hay emergencia los robot van a reposo -> (0,0), eso lo hago en results, aca solo indico la acción
            avalaible_actions.append('IrReposo',posicion)
        return avalaible_actions
    
    def Result(self,state, action):
        tipo_accion, posicion : action

        posicion_robots, Emergencia: state

        posrobot1, posrobot2 = posicion_robots
        if tipo_accion == 'IrReposo':
            posrobot1 = (0,0)
            posrobot2 = (0,0)

        if tipo_accion == 'DefenderConR1':
            posrobot1 = posicion
        if tipo_accion == 'DefenderConR2':
            posrobot2 = posicion
            
        posicion_robots = (posrobot1,posrobot2)

        return (posicion_robots,Emergencia)
    
    def Cost(self,state1,action,state2):
        return 1
    
    
