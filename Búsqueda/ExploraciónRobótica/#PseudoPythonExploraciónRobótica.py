#PseudoPythonExploraciónRobótica

TUNELES = ((5,0),(5,1),(5,3),(5,6),(5,8),(4,1),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(3,1),(3,4),(3,9),(2,1),(2,2),(2,3)
,(2,4),(2,5),(2,6),(2,7),(2,9),(1,2),(1,4),(1,7),(1,8),(1,9),(1,10),(6,1),(6,5),(6,6),(6,10),(7,1),(7,3),(7,6),(7,7),(7,8),
(7,9),(7,10),(8,1),(8,3),(8,7),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8))


ROBOTS = [
("s1", "soporte"), ("e1", "escaneador"),("e2", "escaneador"),("e3", "escaneador")]

lista_robots = []
for robot in ROBOTS:
    lista_robots.append((robot[0],robot[1],1000, (5,0)))

state= (TUNELES,ROBOTS)
class ExploracionRobotica():
    
    def isGoal(self,state):
        tuneles, robot = state
        return len(tuneles) == 0
    
    def Actions(self, state):
        tuneles, lrobot = state
        available_actions = []
        movimientos_posibles = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for rob in lrobot:
            if rob[1] == "escaneador":
                if lrobot["2"]>100:
                    _#Si la bateria es mayor a 500 puedo agregar la posible acción mover siempre y cuando se encuentra en el tunel
                    for pos in movimientos_posibles:
                        posicion = []
                        posicion_robot = rob[3]
                        posicion.append((posicion_robot[0] + pos[0], posicion_robot[1] + pos[1]))
                        if posicion in tuneles:
                            #PuedoAgregar la acción.
                            available_actions.append((robot[0], "mover", (posicion))) #Devuelve el robot, la accion y la posicion adonde se mueve
        
        
        #
        pass
