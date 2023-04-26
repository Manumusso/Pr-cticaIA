#Exploración Robotica
#Variables del problema definidas según funcionalidades solicitadas

problem_variables = ['incrementar_autonomia','terreno_irregulares','cargas_extras','comunicacion_robot']

domains ={}
domains['incrementar_autonomia'] = [
        #desc,consumo,tamañobateria
        ('baterias_chicas',10,5000),
        ('baterias_medianas',20,7500),
        ('baterias_grandes',50,1000),
    ]
domains['terreno_irregulares'] = [
        ('patas_extras',15),
        ('mejores_motores',25),
        ('orugas',50),
]

domains['cargas_extras'] = [
        ('caja_superior',10),
        ('caja_trasera',10),
]
domains['comunicacion_robot'] = [
    ('video_llamadas',10),
    ('radios',5)
]

constraints = {}
consumo_base = 100
baterias_base = 1000




def Controlar_Compat_ParDePatasExtras_CajaSuministroTraseros(variables,values):
    cargas_extras, terrenos_irregulares: values
    has_suministroTrasero = 'caja_trasera' in cargas_extras[0]
    has_patasExtras = 'patas_extras' in terrenos_irregulares[0]
    ##Si ambos son 
    if has_suministroTrasero:
        return not(has_patasExtras)
    return True
    
constraints.append(('cargas_extras','terreno_irregulares'),Controlar_Compat_ParDePatasExtras_CajaSuministroTraseros)

def Compt_Orugas(variables,values):
    terrenos, comunicacion: values
    has_motores = 'mejores_motores' in terrenos[0]
    has_radio = 'radios' in comunicacion[0]
    if has_radio:
        #Si hay radios y mejores motores, la restricción devuelve False
        return not(has_motores)
    return True

constaints.append(('terreno_irregulares','comunicacion_robot'),Compt_Orugas)

def Sistema_Videollamadas(variables,values):
    terrenos, comunicacion: values
    has_patas = 'patas_extras' in terrenos[0]
    has_orugas = 'orugas' in terrenos[0]
    has_radio = 'video_llamadas' in comunicacion[0]
    if has_radio:
        #Si hay radio de videollamada, debe haber además orugas o patas extras
        return has_orugas or has_patas
    return True

constaints.append(('terreno_irregulares','comunicacion_robot'),Sistema_Videollamadas)

#Se desea lograr una autonomía de al menos 50 minutos

def es_autonomo(variables,values):
    var= values[0]
    consumos_extras = 0
    bateria = var[2]
    
    for x in values:
        consumos_extras += x[1]
  
    consumo_t = consumo_base + consumos_extras 
    bateria_resultante = baterias_base + bateria

    autonomia = ((bateria_resultante/consumo_t) >= 50)
    return(autonomia)

constraints.append(((variables_problem),es_autonomo))

#Las baterias  grandes solo se utilizan si tiene las orugas
def es_adm_uruga(variables,values):
    incrementar_autonomia,terreno = values

    #Asigno una variable boolean para comprobar existencia de las baterias grandes
    has_bateriasgrandes = 'baterias_grandes' in incrementar_autonomia[0]

    #Asigno una variable boolean para comprobar existencia de las orugas
    has_orugas = 'orugas' in terreno[0]

    if (has_bateriasgrandes):
    
        #Si la bateria es grande, retornamos True en caso que este la oruga, caso que no False.
        return has_orugas
    else:
        #Si no es bateria grande, no tenemos porque restringir, devolvemos True
        return True
    

constraints.append((('incrementar_autonomia','terreno_irregulares'),es_adm_uruga))