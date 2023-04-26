#ControlDeIncendios2



problem_variables = ["EstaciónCentral","Auxiliar_A","Auxiliar_B"]


ADYACENTES = {'Quintas':['Ciclovialandia'],
              'Ciclovialandia':['Quintas','Centro','42Julio'],
              '42Julio':['BarrioEstandar2','Ciclovialandia','Centro'],
              'Centro':['BarrioEstandar2','42Julio','Ciclovialandia','Aeroclub','BarrioEstandar1'],
              'BarrioEstandar2':['42Julio','Centro','BarrioEstandar1'],
              'BarrioEstandar1':['BarrioEstandar2','Centro','Costanera','BarrioEstandar3','ParqueIndustrial'],
              'Aeroclub':['Centro','Costanera'],
              'ParqueIndustrial':['BarrioEstandar3','BarrioEstandar1'],
              'BarrioEstandar3':['ParqueIndustrial','BarrioEstandar1']
}
domains= {}

Barrios = ['Quintas','Ciclovialandia','42Julio','Centro','BarrioEstandar2','BarrioEstandar1'
           'Aeroclub','ParqueIndustrial','BarrioEstandar3']

#Centro no es considerado.
for var in problem_variables:
    domains[var] = Barrios
    

constraints = {}

domains["Auxiliar_B"].remove('ParqueIndustrial')
domains["Auxiliar_B"].remove('Quintas')
domains["Auxiliar_B"].remove('Aeroclub')

domains["EstaciónCentral"].remove('Centro')
domains["Auxiliar_A"].remove('Centro')
domains["Auxiliar_B"].remove('Centro')

#Restricciones:
#No podemos tener dos variables con el mismo dominio.
#No pueden estar en barrios adyacentes
#El centro no puede alojar estaciones por la falta de espacio físico, pero debe ser considerado a la hora de contar barrios adyacentes
#La casa central tiene que ubicarse en un barrio que tenga al menos otros 3 barrios conectados
#Auxiliar B no puede estar en : Parque Industril, Quintas y Aeroclub.
#La Auxiliar A tiene que estar adyacente al centro
#No puede haber dos estaciones en el mismo barrio

def ControlDiferentes(variables,values):
    var1, var2 : values
    return var1 != var2
for variable1, variable2 in combinatios(problem_variables,2):
    constraints.append((variable1,variable2),ControlDiferentes)


def ControlAdyacentes(variables, values):
    var1, var2, var3 :values
    ##Ejemplo,Si en los adyacentes de Quinta se encuentra Ciclovandia no se puede
    if (var1 in ADYACENTES[var2] or var1 in ADYACENTES[var3]):
        return False
    if (var2 in ADYACENTES[var1] or var2 in ADYACENTES[var3]):
        return False
    if (var3 in ADYACENTES[var1] or var3 in ADYACENTES[var2]):
        return False
    return True

constraints.append((problem_variables,ControlAdyacentes)


##Remuevo de la estación Auxiliar A los NO adyacente al centro.
domains["Auxiliar_A"].remove('ParqueIndustrial')
domains["Auxiliar_A"].remove('BarrioEstandar3')
domains["Auxiliar_A"].remove('Quintas')

