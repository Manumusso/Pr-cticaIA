#Menor cantidad de movimientos posibles, algoritmo de búsqueda.
#El personaje se puede mover de a un casillero por vez en 
#casillas adyacentes,y puedo empujar cajas al moverse.

#Solo puede mover de una caja a la vez, entonces 
#la adyacente no puede tener otra casilla.

#Hay paredes.
#La partida tiene un límite de movimientos posibles.

#Para implementar tengo que mandar una función jugar que recibira como parametro el mapa.
#mapa
#posiciones acutales de las caja y el jugador
#Posiciones Objetivos.
#Cantidad máxima de movimientos.
#Devolver como resultado la secuencia de botones que el jugador debe presionar en el joystick

paredes = []


paredes= (5, 1), (6, 1),(6, 2)

cajas = [(0, 3), (2,4),]

objetivos = [(1, 3), (4, 5)]

jugador=(2,2)

maximos_movimientos = 30
#Posición robot
Estado_Inicial = (jugador,cajas)


class jugar(SearchProblem):
    def Actions(self,state):
        posicion, caj: state
        #Posiciones posibles
        #Mover de una posición vacia a otra vacia
        #Moves a una posición donde haya una caja, entonces tenes que chequear los adyacentes de donde queres mover, 
        # porque si hay otra no tiene sentido, y además si la adyacente es la que estoy con robot tampoco tendria sentido

        available_actions = []

        posibles_movimientos = []

        for var in posibles_movimientos[(-1,0),(1,0),(0,-1),(0,1)]:
            nueva_fila1 = posicion[0]+var
            nueva_columna1 = posicion[1]+var
            nueva_posicion1= (nueva_fila1, nueva_columna1)

            if nueva_posicion1 not in paredes:
                if nueva_posicion1 not in caj:
                    available_actions.append('MoverPersonaje',var)
                else:
                    #DeboControlar donde mover la caja y personaje.
                    posibles_movimientos2 = []
                    for var2 in posibles_movimientos2[(-1,0),(1,0),(0,-1),(0,1)]:
                        nueva_fila2 = posicion[0]+var
                        nueva_columna2 = posicion[1]+var
                        nueva_posicion2= (nueva_fila2, nueva_columna2)
                        if nueva_posicion2 not in paredes:
                            if nueva_posicion2 not in caj and nueva_posicion2!=nueva_posicion1:
                                antigua_posicion_caja = nueva_posicion1
                                available_actions.append('MoverPersonajeYCaja',var,var2,antigua_posicion_caja)
                            
        
        return available_actions
    
    def Results(self,state,action):
        posicion, caj: state
        tipo_accion, posP, posC, antiguaCaja:action
        if tipo_accion == "MoverPersonajeYCaja":
            caj[antiguaCaja].remove()
            caj[posC].append()
            posicion = posP
        if tipo_accion == "MoverPersonaje":
            posicion = posP

        return (posicion,caj)


    def Costs(self,state1,action,state2):
        return 1
    
    def isGoal(self,state):
        posicion, caj: state
        for var in objetivos.values():
            if var not in caj:
                return False
        return True

    def Heuristic(self, state):
        #Como heuristica voy a tener un movimiento por cantidad de caja que falte llegar a la meta-
        posicion, caj: state
        objetivos_Restantes = 0
        for var in objetivos:
            if var not in caj:
                objetivos_Restantes+=1

        return objetivos_Restantes
    

