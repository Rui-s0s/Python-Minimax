from random import randint
from math import dist

# String de multiples lineas con este formato

gato =  r"""
 _._     _,-'""`-._
 (,-.`._,'(       |\`-/|
     `-.-' \ )-`( , o o)
          `-    \`_`"'-
"""

rata = r"""
          _   _
         (_)/` |
       _(_) ^ /
       >\|  -;   _
       \_/    \_/<
        /    ,__/
       ;     |
       |    .-.
       |       )_
     .-\______;__>
    (__..._      _
           `--''` )

"""

# La matriz es una lista que contiene listas y dentro de estas guiones para marcar el tablero

def crear(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('-------')  
        matrix.append(row)
    return matrix

# Los movimientos del gato son como el caballo en ajedrez, moverse en "L"

def cat_moves(pos):
    x, y = pos
    moves = []
    offsets = [(2,1),(2,-1),(-2,1),(-2,-1),
               (1,2),(1,-2),(-1,2),(-1,-2)]
    
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:  
            moves.append((nx, ny))
    return moves

# La rata se mueve en las 8 direcciones como la dama en ajedrez
# Se puede limitar la cantidad de casillas de movimiento

def rat_moves(pos, cat=None, max_range=4):
    x, y = pos
    moves = []
    directions = [(1,0),(-1,0),(0,1),(0,-1),
                  (1,1),(1,-1),(-1,1),(-1,-1)]
    
    for dx, dy in directions:
        nx, ny = x, y
        steps = 0
        while steps < max_range and 0 <= nx+dx < N and 0 <= ny+dy < N:
            nx, ny = nx + dx, ny + dy
            moves.append((nx, ny))
            steps += 1
            if (nx, ny) == cat:
                break
    return moves

# El gato tiene la capacidad de atrapar al raton si es que se encuentra en su area en lugar de estar exactamente en su misma casilla

def mega_knight(a, b):
    ax, ay = a
    bx, by = b
    return max(abs(ax - bx), abs(ay - by))

# Funciones que evaluan valores para el algoritmo de minimax

def is_captured(cat, rat):
    return mega_knight(cat, rat) <= 1

def evaluate(cat, rat):
    if cat == rat:
        return -1000
    return dist(cat, rat)

# ajd convierte una coordenada numerica como [0,0] a su equivalente a un tablero de ajdrez, ["a",1]

def ajd(coordenada:list):
    x, y = coordenada
    ajedrez = [chr(x+97), y+1]  
    return ajedrez

# dja es la funcion opuesta a ajd convirtiendo una coordenada en formato de ajedrez a una coordenada valida

def dja(ajedrez:list):
    x, y = ajedrez
    coordenada = [ord(x)-97, y-1]
    return coordenada

# Minimax es un algoritmo recursivo que se llama a si misma de acuerdo a la profundidad que determinamos
# uno intenta minimizar un valor y otro maximizarlo, en este caso el valor es la distancia
# la profundidad es la cantidad de turnos que va a medir, por ejemplo 3 va a ir de rata, despues gato despues rata otra vez

def minimax(cat, rat, depth, maximizing):
    if depth == 0 or is_captured(cat, rat):
        return evaluate(cat, rat), (cat if not maximizing else rat)

    # Turno de la rata
    if maximizing:  
        best_val = float("-inf")                                    # El valor empieza como infinito negativo para que siempre escoja la primera opcion por default
        best_move = rat
        for mov in rat_moves(rat, cat):                             # Itera en los movimientos posibles
            val, _ = minimax(cat, mov, depth-1, False)              # Prueba como responderia el otro personaje al cambiar la variable maximizing a false y reduce la profundidad 
            if val > best_val:
                best_val = val
                best_move = mov
        return best_val, best_move
    
    # Turno del gato
    # Es el mismo proceso pero este busca minimizar el valor
    else:  
        worst_val = float("inf")                                   
        best_move = cat
        for mov in cat_moves(cat):
            val, _ = minimax(mov, rat, depth-1, True)
            if val < worst_val:
                worst_val = val
                best_move = mov
        return worst_val, best_move

# Para mostrar muestra formateado para poder ver los numeros y letras que hay en un tablero de ajedrez

def mostrar(matrix):
    n = len(matrix)
    for j in range(n):
        etiqueta = n - j
        print(etiqueta, end='    ')
        for k in range(n):
            col = k
            fila_idx = n - 1 - j
            celda = matrix[col][fila_idx]
            end = '\n' if k == n-1 else ' '
            print(celda, end=end)
    print('X', end='    ')
    for k in range(n):
        print(f'   {chr(97+k)}    ', end='')
    print()

# Funcion en que definis los parametros que va a tomar el juego

def jugar(n, max_turns):
    board = crear(n)
    global N
    N = n
    cat = [0, 0]                                                        # Empiezan en esquinas opuestas          
    rat = [n-1, n-1]      

    for turn in range(1, max_turns+1):                                  # Hay un maximo de turnos y el bucle corre por ese numero de turnos
        print(f"\n--- Turno N°: {turn} ---")
        
        board = crear(n)                                                # Cada vez que empieza un nuevo turno creamos un tablero limpio de vuelta
        board[cat[0]][cat[1]] = "=^-_-^="                               # Ponemos las posiciones en las que estuvieron en el turno anterior
        board[rat[0]][rat[1]] = "<:3 )~~"
        mostrar(board)                                                  # Imprimimos el tablero
        
        # Movimiento del gato
        legal_moves = cat_moves(tuple(cat))
        print("Movimientos posibles:", [ajd(m) for m in legal_moves])   # Mostramos los movimientos validos para facilitar la eleccion

        valid = False
        while not valid:                                                # Bucle en que verificamos que ingrese adecuadamente los movimientos
            mov = input("Su movimiento: ").lower()
            if len(mov) == 2 and mov[0].isalpha() and mov[1].isdigit():
                col, row = mov[0], int(mov[1])
                chosen = dja([col, row]) 

                if tuple(chosen) in legal_moves:
                    cat = chosen
                    valid = True
                else:
                    print("❌ Movimiento invalido, pruebe otra vez")
            else:
                print("❌ Input invalido, use notacion de ajedrez")

        if is_captured(cat, rat):                                       # Verifica si con ese movimeinto atrapa al raton y rompe el bucle
            print("La rata fue atrapada!!!")
            print(gato)
            return
        
        # Movimiento de la rata (IA)
        _, best_rat = minimax(tuple(cat), tuple(rat), depth=3, maximizing=True)
        rat = list(best_rat)
        print("La rata se escapa a:", ajd(rat))
        
    
    print(f"La rata sobrevivio {max_turns} turnos y escapo")
    print(rata)


# Elegimos el tamanyo del tablero y el maximo de turnos
jugar(8,4) 