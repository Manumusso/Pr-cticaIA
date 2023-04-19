#Robot de exploración luna
#   0   1   2   3   
#   -   B   M   M
#   -   -   -   -
#   M   -   -   -   
#   -   M   -   -

MUESTRAS = ((0,2),(0,3),(2,0),(3,1))
BATERIA = 1000
GASTO_IR = 100
GASTO_DEPOSITAR_MUESTRA = 50
GASTO_TOMAR_MUESTRA = 250

BASE = (0,1)
Muestras_Depositadas = []
# Posición del robot,bateria, muestras
INITIAL_STATE= (BASE, BATERIA, Muestras_Depositadas)

def CalcularGastoBateria(posicion):
    posx,posy = posicion
    MovimientosVuelta = abs (BASE[0]-posx) + abs (BASE[1]-posy)

    return MovimientosVuelta * GASTO_IR

class ExploracionLunar(SearchProblem):
    
    def isGoal(self, state):
        posicion_robot, bat, Muestra_Depositadas = state
        return len(MUESTRAS) == len(Muestra_Depositadas)

    def actions(self,state):
        posicion_robot, bat, Muestra_Depositadas = state
        fila, columna = posicion_robot
        available_actions = []

        if posicion_robot in BASE:
            #Si estoy en la base, debería poder cargarlo.
            available_actions.append('Cargar',posicion_robot)

            #Si tengo una muestra pendiente de depositar, debo poder depositarla.
            if len(MUESTRAS) != 0:
                #En este punto con saber que la tarea es depositar sería suficiente.
                available_actions.append('DepositarMuestra',posicion_robot)

        if posicion_robot in MUESTRAS:
            #Si estoy en una posición de interes, debo poder tomar la muestra.
            available_actions.append('AgregarMuestra',posicion_robot)


        if bat > CalcularGastoBateria(posicion_robot):
            #Puedo ir a cualquier lugar mientras se encuentre en el tablero que me permita 
            # llegar a la base para cargar según la bateria del momento
            movimientos_posibles = []
            if fila>0:
                movimientos_posibles.append(fila-1,columna)
            if fila <3:
                movimientos_posibles.append(fila+1,columna)
            if columna>0:
                movimientos_posibles.append(fila,columna-1)
            if columna<3:
                movimientos_posibles.append(fila,columna+1)

            for mov in movimientos_posibles:
                available_actions.append('Ir',mov)

            return available_actions

    def results(self, state, action):
        posicion_robot, bat, Muestra_Depositadas = state
        tipo_accion, robot = action
        if tipo_accion == 'Ir':
            posicion_robot = robot
            bat -= GASTO_IR
        if tipo_accion == 'DepositarMuestra':
            Muestra_Depositadas.append(posicion_robot)
            bat -= GASTO_DEPOSITAR_MUESTRA
        if tipo_accion == 'AgregarMuestra':
            bat -= GASTO_TOMAR_MUESTRA
        if tipo_accion == 'Cargar':
            bat = BATERIA
        return (posicion_robot,bat,Muestra_Depositadas)


    def cost(self,state1,action,state2):
        tipo_accion, robot = action
        costo = 0
        if tipo_accion == 'Ir':
            costo = 5
        if tipo_accion == 'DepositarMuestra':
            costo = 10
        if tipo_accion == 'AgregarMuestra':
            costo = 15
        if tipo_accion == 'Cargar':
            costo = 30
        return costo

    def heuristic(self, state):
        posicion_robot, bat, Muestra_Depositadas = state
        costo_heuristic = 0
        #Por cada muestra que falte depositar, 
        # como minimo va a tener que ir a cada posición sin contar si la actual esta en una zona de interes.
        
        for muestra in MUESTRAS:
            if muestra not in Muestra_Depositadas and posicion_robot != muestra:
                costo_heuristic += 5

        return costo_heuristic 




                    