import threading

# Sudoku para teste
sudoku = [
    [2, 3, 7, 8, 4, 1, 5, 6, 9],
    [1, 8, 6, 7, 9, 5, 2, 4, 3],
    [5, 9, 4, 3, 2, 6, 7, 1, 8],
    [3, 1, 5, 6, 7, 4, 8, 9, 2],
    [4, 6, 9, 5, 8, 2, 1, 3, 7],
    [7, 2, 8, 1, 3, 9, 4, 5, 6],
    [6, 4, 2, 9, 1, 8, 3, 7, 5],
    [8, 5, 3, 4, 6, 7, 9, 2, 1],
    [9, 7, 1, 2, 5, 3, 6, 8, 4]
]

# Usando contadores - sem valores iniciais
trava = threading.Lock()
contador_validos = 0

def verificar_linha(indice_linha):
    global contador_validos
    numeros = sudoku[indice_linha]
    if sorted(numeros) == list(range(1, 10)):
        with trava:
            contador_validos += 1

def verificar_coluna(indice_coluna):
    global contador_validos
    numeros = [sudoku[i][indice_coluna] for i in range(9)]
    if sorted(numeros) == list(range(1, 10)):
        with trava:
            contador_validos += 1

def verificar_subgrid(indice_grid, linha_inicial, coluna_inicial):
    global contador_validos
    numeros = []
    for i in range(linha_inicial, linha_inicial + 3):
        for j in range(coluna_inicial, coluna_inicial + 3):
            numeros.append(sudoku[i][j])
    
    if sorted(numeros) == list(range(1, 10)):
        with trava:
            contador_validos += 1

def main():
    threads = []
    
    # Threads para linhas
    for i in range(9):
        t = threading.Thread(target=verificar_linha, args=(i,))
        threads.append(t)
    
    # Threads para colunas
    for i in range(9):
        t = threading.Thread(target=verificar_coluna, args=(i,))
        threads.append(t)
    
    # Threads para subgrids 3x3
    indice_grid = 0
    for linha in range(0, 9, 3):
        for coluna in range(0, 9, 3):
            t = threading.Thread(target=verificar_subgrid, args=(indice_grid, linha, coluna))
            threads.append(t)
            indice_grid += 1
    
    # Inicia todas as threads
    for t in threads:
        t.start()
    
    # Aguarda todas terminarem
    for t in threads:
        t.join()
    
    # Se todas as 27 verificações (9+9+9) foram válidas
    if contador_validos == 27:
        print("Sudoku válido")
    else:
        print("Sudoku inválido")

main()