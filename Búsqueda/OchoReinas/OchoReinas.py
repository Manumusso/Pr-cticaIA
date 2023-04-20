
#Problema ocho reinas.



#No puedo plantear un goal true o false, debo generar un value, porque puedo llegar a varios estados metas.
#State
#El estado inicial debe variar en cuanto a contenido porque sino siempre tendrá el mismo value según las piezas ingresada.

#El estado se compone der una tupla, donde cada posición será la columna y el valor contenidola fila teniendo en cuenta que no se pueden atacar


#INITIAL_STATE = (1,0,0,2,3,4,5,6,7)

#Representación del estado anterior

#   -   r   r   -   -   -   -   -   -
#   r   -   -   -   -   -   -   -   -
#   -   -   -   r   -   -   -   -   -   
#   -   -   -   -   r   -   -   -   -
#   -   -   -   -   -   r   -   -   -
#   -   -   -   -   -   -   r   -   -
#   -   -   -   -   -   -   -   r   -
#   -   -   -   -   -   -   -   -   r

                            diferenciaFilas = abs (queen1-queen2)
                            diferenciaColumnas = abs (posicion1-posicion2)
#Actions
# No puedo bloquear estados que una acción derive que se ataquen, porque podría encontrar el estado optimo al pasar por un estado donde se ataquen, entonces voy a limitarme en mover dentro del tablero por fila(+1,-1).

def enFila(self,fila):
    return all(0<= c <= 6 for c in fila)

class OchoReinas(SearchProblem):
 
    def actions(self,state):
        avalaible_actions = []
        for pos, value in state.items:
            posibles_movimientos = []
            for x in posibles_movimientos[1,-1]:
                nuevaFila = value + x
                if enFila(nuevaFila):
                    #Anterior fila, nueva fila
                    avalaible_actions.append(value,nuevaFila);
        
        return avalaible_actions
    
    def Result(self, state, action):
        value, nueva_fila = action
        state[value] = nueva_fila

        return state
    #Que tan bueno es el estado que tenemos?
    def value (self, state):
            attacks = 0
            #Que tantas reinas nos atacan.
            #Mejores estados tienen que tener value más altos.
            #Entonces cuanto menos se ataquen mejor.
            #Podríamos negativo de  la cantidad de reinas que se atacan, entonces si las reinas se atacan en 5 casos es peor que se ataquen en 0
            #En la misma columna no se podrían atacar, por como definimos el estado. Pero las filas SI.
            for posicion1,queen1 in state:
                for posicion2,queen2 in state:     
                    #Con posición me aseguro que no sea la misma reina, es decir que no coincidan las columnas
                    if posicion1 != posicion2:
                        #Ahora tengo que verificar que se ataquen, es decir que  esten en la misma fila para poder contar ataques.
                        if queen1 == queen2:
                            attacks += 1
                        else: 
                            #Chequear la diagonal
                            diferenciaFilas = abs (queen1-queen2)
                            diferenciaColumnas = abs (posicion1-posicion2)
                            if diferenciaFilas == diferenciaColumnas:
                                  attacks += 1
            return attacks

    
    def Generate_Random_State(self,state):
        state= []
        for queen in range(8):
            queen_row = randint(0,7)
            state.append(queen_row)
        return state