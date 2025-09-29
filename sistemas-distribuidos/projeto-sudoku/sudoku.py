import threading

# Sudoku de exemplo (válido)
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

# Variável global para resultado  
lock = threading.Lock()
results = {"rows": [True] * 9, "cols": [True] * 9, "subgrids": [True] * 9}

# Função para verificar uma linha
def check_row(row_index):
    row = sudoku[row_index]
    if sorted(row) != list(range(1, 10)):
        with lock:
            results["rows"][row_index] = False

# Função para verificar uma coluna
def check_col(col_index):
    column = [sudoku[row][col_index] for row in range(9)]
    if sorted(column) != list(range(1, 10)):
        with lock:
            results["cols"][col_index] = False

# Função para verificar subgrid 3x3
def check_subgrid(index, start_row, start_col):
    nums = []
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            nums.append(sudoku[r][c])
    if sorted(nums) != list(range(1, 10)):
        with lock:
            results["subgrids"][index] = False

# Criar threads
threads = []

# 9 threads para as linhas
for i in range(9):
    t = threading.Thread(target=check_row, args=(i,))
    threads.append(t)

# 9 threads para as colunas  
for i in range(9):
    t = threading.Thread(target=check_col, args=(i,))
    threads.append(t)

# 9 threads para os subgrids
index = 0
for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        t = threading.Thread(target=check_subgrid, args=(index, r, c))
        threads.append(t)
        index += 1

# Iniciar todas as threads
for t in threads:
    t.start()

# Esperar todas finalizarem
for t in threads:
    t.join()

# Resultado final
if all(results["rows"]) and all(results["cols"]) and all(results["subgrids"]):
    print("O Sudoku é válido!")
else:
    print("O Sudoku NÃO é válido!")
