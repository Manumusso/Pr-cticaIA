#TrasladoPresidentes

#Tengo que trasladar 6 presedientes del auditorio hacia la sala de conferencias pasando por el hall de entrada
# Puedo mover de 1 a 2 presidentes, de a una habitación por movimiento avanzando y nunca retrocediendo
# Los escoltas se pueden mover por cualquier habitación
# 2 Capitalistas, 2 comunistas y 2 centristas.

# Nunca pueden quedar dos presidentes de la misma facción solos en la misma sala, sin presidentes de otras facciones, porque van a pensar que estan conspirando
# Cuando dos presidentes de la misma facción están separados, solo puede ser en salas adyacentes, No puede quedar un presidente en cada extremo si son de la misma facción, porque 
# se sentirian muy aislados.


Auditorio = ['P1','P2','P3','P4', 'P5', 'P6']
Hall = []
SalaDePrensa = []

Presidentes = {'P1':'Capitalista',
               'P2':'Capitalista',
               'P3':'Comunista',
               'P4':'Comunista',
               'P5':'Centrista',
               'P6':'Centrista',
               }
#Cada tupla representa la habitación, y van a contener los identificadores del presidente que se encuentra en la sala
EstadoInicial = (Auditorio,Hall,SalaDePrensa)

class TrasladoPresidentes(SearchProblem):
    def isGoal(self,state):
        lauditorio, lhall, lSalaDePrensa : state
        return len(lSalaDePrensa) == 6
