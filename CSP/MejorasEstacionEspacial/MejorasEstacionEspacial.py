#Mejoras estación espacial.





problem_variables = ['Mejora1','Mejora2','Mejora3']



domains = {}


for var in problem_variables:
    domains[var] = [
        ('Bat',12.5,300),
        ('Brazo',60,50),
        ('Ventana', 100,550),
        ('Antena',20,30),
        ('LabPlantas',80,250),
        ('LabExpFisicos',75,300),
        ('Compu',50,20),
        ('Reciclador',30,100),
    ]

def different(variables,values):
    improv1, improv2 = values
    return improv1 != improv2

for variable1,variable2 in combinations(problem_variables,2):
    constraints.append((variable1,variable2),different)

#Variable 1 podría ser ('Bat',12.5,300)
#Variable 2 podría ser ('LabExpFisicos',75,300)


def ControlarDinero(variables,values):
    dipositivos: values
    monto= 0
    #El for es con variable o con problem_variables?
    for x in values:
        #De cada dispositivo sumo el monto
        monto += x[1]
    #Si el monto total de equipamiento no supera 150 millones, entonces la restriccion se cumple(Devuelve True)    
    return monto<=150


#Duda, deberia acumular al llamar la función o dentro de la función
#for x in problem_variables:
#    contraints.append((x),ControlarDinero)
#Este for se puede reemplazar pasando el parametro general

contraints.append((problem_variables),ControlarDinero)
#La restricción anterior la dejamos como no binaria, pero TODAS SE podrían hacer
#Entonces, restriccion dinero programada con restricción global de 3 variables.



def ControlarCantidad(variables,values):
    dipositivos: values
    cantidad= 0
    #El for es con variable o con problem_variables?
    for x in values:
        #De cada dispositivo sumo el monto
        cantidad += x[2]
    #Si el monto total de equipamiento no supera 150 millones, entonces la restriccion se cumple(Devuelve True)    
    return cantidad<=1000

#OJO CON LIMITAR DE ESTA MANERA. 
domains["mejora1"].remove(("exp_plantas",80,250))
domains["mejora2"].remove(("exp_fisicos",80,250))
domains["mejora3"].remove(("exp_fisicos",80,250))
#En este caso no se puede  podría pasar:
#1 = "exp_fisicos"
#2 = "exp_plantas"
# Y no sería compatible

#Si seguimos insistiendo en modificarl os dominios, la opción sería:
#domains["mejora2"].remove(("exp_plantas",80,250))
#domains["mejora2"].remove(("exp_fisicos",80,250))

#domains["mejora3"].remove(("exp_planta",80,250))
#domains["mejora3"].remove(("exp_fisicos",80,250))

for x in problem_variables:
    contraints.append((x),ControlarCantidad)
    dipositivos: values
    cantidad= 0
    #El for es con variable o con problem_variables?
    for x in values:
        #De cada dispositivo sumo el monto
        if  values[x] == 'LabPlantas':

    #Si el monto total de equipamiento no supera 150 millones, entonces la restriccion se cumple(Devuelve True)    
    return cantidad<=1000

def ControlarCompatibles_LabFisico_Plantas(variables, values):
    pass


for x in problem_variables:
    contraints.append((x),ControlarCompatibles_LabFisico_Plantas)
