#Sudoku
# Codigo realizado en clase 9 2021 IA  - UCSE Por Fisa + Curso
#No se pueden repetir los números en las columnas, filas, diagonales ni en el mismo cuadrado.
#Tablero -> Variables
#Dominio -> [0,1,2,3,4,5,6,7,8,9]

#Si me dice el tablero si o si tiene que tener casilleros vacios, ahi deberia analizar si es dominio.

#El tablero ya tiene variables con un values definido, 
    #Se puede plantear de dos maneras:
        # Decir que las variables las posiciones de la grilla,  y en su dominio algunas tengan restricciones
        # o directamente decir que donde hay valores no son variables, pero sería más complicado porque al ingresar 
        # debería verificar que no estoy repitiendo números. Conclusión definir como una variable.(Más facil de programar)
       


columns = list(range(9))
rows = list(range(9))


problem_variables = [
    (row, col)
    for row in rows
    for col in columns
]

domains = {}
for coords in problem_variables:
    domains[coords] = {1,2,3,4,5,6,7,8,9}

constraints = []


def cells_are_different(variables,values):
    dig1,dig2 : values
    return dig1 != dig2

##Coordenadas en la fila.
for row in rows:
    coords_in_row = [
        (row, col)
        for col in columns
    ]
    for coords1, coords2 in combinations(coords_in_row, 2):
        constraints.append(
            ((coords1,coords2), cells_are_different)
        )


##Coordenadas en la columna
for col in columns:
    coords_in_col = [
        (row, col)
        for row in rows
    ]
    for coords1, coords2 in combinations(coords_in_col, 2):
        constraints.append(
            ((coords1,coords2), cells_are_different)
        )


#Falta:
    # Limpiar y dejar solo 1 valor en los dominios celdas ya rellenas   
    # Agregar todas las restricciones de que sean diferentes las celdas

#Limpiar y dejar solo un dominio en las celdas ya rellenas.
#A3
domains[(0,2)] = 3
#A5
domains[(0,4)] = 2
#A7
domains[(0,6)] = 6
#B1
domains[(1,0)] = 9
#B4
domains[(1,3)] = 3
#B6
domains[(1,3)] = 5
#B9
domains[(1,8)] = 1

#C3
domains[(2,2)] = 1
#C4
domains[(2,7)] = 8
#C6
domains[(2,5)] = 6

#Plantear restricciones para los cuadrados.
def is_quadrant(celda):
    row, col = celda
    return row // 3, col // 3

for x in range(0,2):
    for y in range(0,2):
        cells_in_quadrant = []
        for cell in problem_variables:
            row_q, col_q = is_quadrant(cell)
            if row_q == x and col_q==y:
                cells_in_quadrant.append(cell)
            for cell1, cell2 in combinations(cells_in_quadrant,2):
                constraints.append(
                ((cell1,cell2), cells_are_different)
                )
                




