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

def calcularPartido(sala, partido):
    
    contadorMismoPartido = 0
    contadorDiferentePartido = 0
    for presidente in sala:
        if Presidentes[presidente] == partido:
            contadorMismoPartido += 1

        else:
            contadorDiferentePartido += 1
       
    return (contadorMismoPartido,contadorDiferentePartido)



class TrasladoPresidentes(SearchProblem):
    def isGoal(self,state):
        lauditorio, lhall, lSalaDePrensa : state
        return len(lSalaDePrensa) == 6


    def actions(selt,state):
        lauditorio, lhall, lSalaDePrensa : state
        # Cuento la cantidad de presidentes del mismo partido y diferentes.
        avalaible_actions = []

        CantidadMovimientosPresidentes = 0
        #Recorro las sala, por ejemplo Auditorio
        
        for x in lauditorio:
            if CantidadMovimientosPresidentes <= 2:
                cantidades = calcularPartido(lauditorio,Presidentes[x])

                MismoPartido, DiferentePartido = cantidades
                MismoPartido -= 1

                cantidadesExtremo = calcularPartido(lSalaDePrensa)
                cantidadesExtremoIguales,  : cantidadesExtremo
                if DiferentePartido>0 and cantidadesExtremoIguales == 0:
                    #No pueden quedar dos presidentes del mismo partido en la sala
                    #Si quiero mover el presidente Capitalista y hay otro de partido, lo podría mover salvo que su compañero del mismo partido no este en una posición adyacente.
                    avalaible_actions.append('IrHall', x)
                    CantidadMovimientosPresidentes += 1
                else:
                    if MismoPartido == 0 and cantidadesExtremoIguales == 0:
                        avalaible_actions.append('IrHall', x)
                        CantidadMovimientosPresidentes += 1
                        #Si no hay de diferentes partidos, y no hay otro del mismo. Quedo solari entonces lo puedo mover(siempre y cuando el compañero este en la sala adyacente)
        for x in lhall:
            if CantidadMovimientosPresidentes <= 2:
                cantidades = calcularPartido(lauditorio,Presidentes[x])

                MismoPartido, DiferentePartido = cantidades
                MismoPartido -= 1

                if DiferentePartido>0:
                    #No pueden quedar dos presidentes del mismo partido en la sala
                    #Si quiero mover el presidente Capitalista y hay otro de partido, lo podría mover salvo que su compañero del mismo partido no este en una posición adyacente.
                    avalaible_actions.append('IrSalaDePrensa', x)
                    CantidadMovimientosPresidentes += 1
                else:
                    if MismoPartido == 0:
                        avalaible_actions.append('IrSalaDePrensa', x)
                        CantidadMovimientosPresidentes += 1
                        #Si no hay de diferentes partidos, y no hay otro del mismo. Quedo solari entonces lo puedo mover(siempre y cuando el compañero este en la sala adyacente
        
        return avalaible_actions
    

    def results(self,state,action):
        tipo_accion, presidente: action
        lauditorio, lhall, lSalaDePrensa : state
        if tipo_accion == 'IrHall':
            ##Debo mover el presidente y removerlo del auditorio
            lhall.append(presidente)
            lauditorio.remove(presidente)
        if tipo_accion == 'IrSalaDePrensa':
            lhall.remove(presidente)
            lSalaDePrensa.append(presidente)
        
        return (lauditorio,lhall,lSalaDePrensa)
    
    def cost(self, state):
        return 1
    
    def heuristic(self,state):
        #Un movimiento por presidentes que faltan llegar a la sala de prensa según el estado actual.
        lauditorio, lhall, lSalaDePrensa : state
        costo_heuristic = 6 - len(lSalaDePrensa)
        return costo_heuristic