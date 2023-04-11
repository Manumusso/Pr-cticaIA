from simpleai.search import SearchProblem

#	1	2	4
#	x	3	5
#	6	8	7

INITIAL_1 = (
	(1,	4,	2),
    (None, 3, 5),
    (6, 7, 8),
)

#INITIAL_2 = [ 1,2,4,None,3,5,6,8,7]
META = (
       (0,1,2),
       (3,4,5),
       (6,7,8),
)
#Necesito saber en que lugar se encuentra "vacio" para poder determinar las acciones posibles.
function DeterminarPos(pieza,state):
    for row_index, row in enumerate(state):
        #Recorro las filas
        # Ejemplo
        #Row index = 0
        # rows = 1,4,2
    
        for col_index, current_piece in enumerate(col_index):
            #Recorro las columnas ejemplo
            # col_index = 0
            # current_piece = 1
            if current_piece == piece:
                return row_index, col_index
        
#ResoluciónMediante algoritmos de búsqueda no informada
class EightPuzzle(SearchProblem):
    
    def is_goal(self, state):
    	return state == GOAL  
    
    def actions(self, state):
        #Necesito la posición del vacio.
        empty_row, empty_col = DeterminarPos(None,state)
        available_actions = []
        if empty_row > 0:
            #Si es mayor a 0 es posible mover arriba
            #Tiene el número de la pieza que quiero mover
            #Por lo tantos las acciones tendran el valor de la pieza que podemos intercambiar con el lugar vacio.
            available_actions.append(state[empty_row -1][empty_col])
        if empty_row <2:
            available_actions.append(state[empty_row +1][empty_col])
       	if empty_col > 0:
            available_actions.append(state[empty_row][empty_col-1])
        if empty_col <2:
            available_actions.append(state[empty_row][empty_col+1])   
            
        return available_actions
    
    def cost(self, state1 , action, state2):
        return 1
    
    def result(self, state, action):    
        #Hay que intercambiar la pieza None con el valor de la pieza que vamos a mover.
        empty_row, empty_col = DeterminarPos(None,state)
        pieza_Valor = action
        #Según lo que percibo del estado actual, buscar la posición de la pieza que deseo mover.
        empty_rowPV, empty_colPV = DeterminarPos(pieza_Valor,state)
        #Ya tengo ambas posiciones, ahora hay que intercambiarlas
        #Ya sabemos que una de las dos variables el valor es 0.
        
        #Este paso es necesario por los objetos inmutables.
        state_as_lists = list(list(row) for row in state)
        
        
        state_as_lists[empty_row][empty_col] = action
        state_as_lists[empty_rowPV][empty_colPV] = 0
        
        new_state = tuple(tuple(row) for row in state_as_lists)
        return new_state
        