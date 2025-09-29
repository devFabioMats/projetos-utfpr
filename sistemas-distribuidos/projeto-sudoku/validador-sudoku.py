"""
Nome..: FABIO EIZO RODRIGUEZ MATSUMOTO
Turma.: ES45A-ES51 / SISTEMAS DISTRIBUIDOS
Data Entrega..: 29/09/2025 - 23:59
Enunciado..: Exercício do livro Fundamentos de Sistemas Operacionais de A. Silberschatz, 
P. Galvin, G. Gagne página 110. Elaboração de uma aplicação com múltiplos threads 
que determine se a solução para um quebra-cabeça Sudoku é válida.
"""

import threading

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

trava = threading.Lock()
resultado_linhas = [True] * 9
resultado_colunas = [True] * 9  
resultado_subgrids = [True] * 9

def verificar_linha(indice):
    numeros_linha = sudoku[indice]
    
    if sorted(numeros_linha) != list(range(1, 10)):
        with trava:
            resultado_linhas[indice] = False


def verificar_coluna(indice):    
    numeros_coluna = []
    linha = 0
    
    for linha in range(9):
        numeros_coluna.append(sudoku[linha][indice])
    
    if sorted(numeros_coluna) != list(range(1, 10)):
        with trava:
            resultado_colunas[indice] = False


def verificar_subgrid(indice_grid, linha_inicio, coluna_inicio):
    numeros_subgrid = []
    i = 0
    j = 0
    
    for i in range(linha_inicio, linha_inicio + 3):
        for j in range(coluna_inicio, coluna_inicio + 3):
            numeros_subgrid.append(sudoku[i][j])
    
    if sorted(numeros_subgrid) != list(range(1, 10)):
        with trava:
            resultado_subgrids[indice_grid] = False


def main():        
    lista_threads = []
    i = 0
    
    for i in range(9):
        thread_linha = threading.Thread(target=verificar_linha, args=(i,))
        lista_threads.append(thread_linha)

    for i in range(9):
        thread_coluna = threading.Thread(target=verificar_coluna, args=(i,))
        lista_threads.append(thread_coluna)

    indice_subgrid = 0
    linha = 0
    coluna = 0
    
    for linha in range(0, 9, 3):
        for coluna in range(0, 9, 3):
            thread_subgrid = threading.Thread(target=verificar_subgrid, args=(indice_subgrid, linha, coluna))
            lista_threads.append(thread_subgrid)
            indice_subgrid = indice_subgrid + 1
    
    for thread in lista_threads:
        thread.start()
    
    for thread in lista_threads:
        thread.join()
    
    todas_linhas_validas = all(resultado_linhas)
    todas_colunas_validas = all(resultado_colunas)
    todos_subgrids_validos = all(resultado_subgrids)
    
    sudoku_valido = todas_linhas_validas and todas_colunas_validas and todos_subgrids_validos
    
    if sudoku_valido:
        print("RESULTADO: O Sudoku é VÁLIDO!")
    else:
        print("RESULTADO: O Sudoku é INVÁLIDO!")

main()