#PseudoPython

STATE = ('E', {'E':0, 'L':10,'D':10,'C':600,'B':30})
MAPA = {'E':('L'),'L':('E','C','D'), 'D':('L'), 'C':('B','L'),'B':('C')}
class ControlIncendios:
    def isGoal(self,state):
        habitación_bombero, fuegos_Restantes = state
        for x,value in fuegos_Restantes.items():
            if value > 0:
                return False
        return True
    
    def Actions(self,state):
        habitación_bombero, fuegos_Restantes = state
        available_actions = []
        if fuegos_Restantes[habitación_bombero] > 0:
            #Si la habitación del bombero tiene fuego, entonces hay que tener en cuenta la acción rociar en la habitación actual.
            # Se pasa como parametro una tupla de dos elementos, el tipo de acción y la cantidad de fuego de la habitación.
            available_actions.append('Rociar',fuegos_Restantes[habitación_bombero])
            #Se agregan todas las posibles acciones ir que se puedan ir desde el estado actual, según el mapa definido
            for x,value in MAPA[habitación_bombero].items():
                available_actions.append('IR',value)
        return available_actions
        
    def Results(self,state,action):
        habitación_bombero, fuegos_Restantes = state
        tipo_accion, value = action
        if tipo_accion == 'Ir':
            habitación_bombero = value
        if tipo_accion == 'Rociar':
            fuegos_Restantes[habitación_bombero] -= value

        return state(habitación_bombero,fuegos_Restantes)


    def Cost(self,state1,action,state2):
        tipo_accion, value = action
        if tipo_accion == 'Ir':
            return 5
        if tipo_accion == 'Rociar':
            return value
    
    def Heuristic(Self,state):
        #La heuristica esta definida como las habitaciones que falta apagar fuego según el estado y además  5 segundos por habitación con fuego sin contar la que estoy parado 
        habitación_bombero, fuegos_Restantes = state
        costo = 0
        for x,value in fuegos_Restantes[1]:
            costo += fuegos_Restantes[1]
            if value >0 and fuegos_Restantes[habitación_bombero] != fuegos_Restantes[1]:
                costo += 5
        return costo
