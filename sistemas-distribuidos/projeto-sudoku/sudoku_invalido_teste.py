import threading

# Sudoku de exemplo (INVÁLIDO - linha 1 tem dois 2s)
sudoku = [
    [2, 2, 7, 8, 4, 1, 5, 6, 9],  # Dois 2s nesta linha
    [1, 8, 6, 7, 9, 5, 2, 4, 3],
    [5, 9, 4, 3, 2, 6, 7, 1, 8],
    [3, 1, 5, 6, 7, 4, 8, 9, 2],
    [4, 6, 9, 5, 8, 2, 1, 3, 7],
    [7, 2, 8, 1, 3, 9, 4, 5, 6],
    [6, 4, 2, 9, 1, 8, 3, 7, 5],
    [8, 5, 3, 4, 6, 7, 9, 2, 1],
    [9, 7, 1, 2, 5, 3, 6, 8, 4]
]

# Variáveis globais para resultados com lock para thread safety
results_lock = threading.Lock()
results = {
    "rows": [True] * 9, 
    "cols": [True] * 9, 
    "subgrids": [True] * 9
}

def is_valid_set(numbers):
    """Verifica se um conjunto contém todos os números de 1 a 9"""
    return sorted(numbers) == list(range(1, 10))

# Função para verificar uma linha específica
def check_row(row_index):
    row = sudoku[row_index]
    with results_lock:
        results["rows"][row_index] = is_valid_set(row)
    print(f"Thread linha {row_index + 1}: {'✅ Válida' if results['rows'][row_index] else '❌ Inválida'}")

# Função para verificar uma coluna específica
def check_col(col_index):
    column = [sudoku[row][col_index] for row in range(9)]
    with results_lock:
        results["cols"][col_index] = is_valid_set(column)
    print(f"Thread coluna {col_index + 1}: {'✅ Válida' if results['cols'][col_index] else '❌ Inválida'}")

# Função para verificar um subgrid 3x3 específico
def check_subgrid(index, start_row, start_col):
    nums = []
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            nums.append(sudoku[r][c])
    
    with results_lock:
        results["subgrids"][index] = is_valid_set(nums)
    print(f"Thread subgrid {index + 1} ({start_row//3 + 1},{start_col//3 + 1}): {'✅ Válido' if results['subgrids'][index] else '❌ Inválido'}")

def main():
    print("🧩 Testando Sudoku INVÁLIDO com múltiplas threads...\n")
    
    threads = []
    
    # Criar 9 threads para verificar linhas
    for i in range(9):
        t = threading.Thread(target=check_row, args=(i,), name=f"Row-{i+1}")
        threads.append(t)
    
    # Criar 9 threads para verificar colunas
    for i in range(9):
        t = threading.Thread(target=check_col, args=(i,), name=f"Col-{i+1}")
        threads.append(t)
    
    # Criar 9 threads para verificar subgrids 3x3
    index = 0
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            t = threading.Thread(target=check_subgrid, args=(index, r, c), name=f"Subgrid-{index+1}")
            threads.append(t)
            index += 1
    
    print(f"🚀 Iniciando {len(threads)} threads...\n")
    
    # Iniciar todas as threads
    for t in threads:
        t.start()
    
    # Esperar todas finalizarem
    for t in threads:
        t.join()
    
    print("\n" + "="*50)
    print("📋 RELATÓRIO FINAL:")
    print("="*50)
    
    # Verificar resultados das linhas
    invalid_rows = [i+1 for i, valid in enumerate(results["rows"]) if not valid]
    if invalid_rows:
        print(f"❌ Linhas inválidas: {invalid_rows}")
    else:
        print("✅ Todas as linhas são válidas")
    
    # Verificar resultados das colunas  
    invalid_cols = [i+1 for i, valid in enumerate(results["cols"]) if not valid]
    if invalid_cols:
        print(f"❌ Colunas inválidas: {invalid_cols}")
    else:
        print("✅ Todas as colunas são válidas")
    
    # Verificar resultados dos subgrids
    invalid_subgrids = [i+1 for i, valid in enumerate(results["subgrids"]) if not valid]
    if invalid_subgrids:
        print(f"❌ Subgrids inválidos: {invalid_subgrids}")
    else:
        print("✅ Todos os subgrids são válidos")
    
    # Resultado final
    is_valid = all(results["rows"]) and all(results["cols"]) and all(results["subgrids"])
    
    print("\n" + "="*50)
    if is_valid:
        print("🎉 RESULTADO: O Sudoku é VÁLIDO!")
    else:
        print("💥 RESULTADO: O Sudoku é INVÁLIDO!")
    print("="*50)

if __name__ == "__main__":
    main()