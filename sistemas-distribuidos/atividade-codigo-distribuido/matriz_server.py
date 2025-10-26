#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
import random

class MatrizServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []
        self.results = {}
        self.matriz_a = []
        self.matriz_b = []
        self.resultado = []
        self.n = 0
        
    def gerar_matrizes(self, tamanho):
        self.n = tamanho
        print(f"Gerando matrizes {tamanho}x{tamanho}")
        
        self.matriz_a = [[random.randint(1, 10) for _ in range(tamanho)] for _ in range(tamanho)]
        self.matriz_b = [[random.randint(1, 10) for _ in range(tamanho)] for _ in range(tamanho)]
        self.resultado = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
        
        print("Matriz A:")
        for linha in self.matriz_a:
            print(linha)
        print("Matriz B:")  
        for linha in self.matriz_b:
            print(linha)
            
    def multiplicacao_sequencial(self):
        print("Iniciando multiplicacao sequencial...")
        inicio = time.time()
        
        resultado_seq = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    resultado_seq[i][j] += self.matriz_a[i][k] * self.matriz_b[k][j]
                    
        fim = time.time()
        tempo_seq = (fim - inicio) * 1000
        print(f"Tempo sequencial: {tempo_seq:.2f} ms")
        return tempo_seq
        
    def multiplicacao_paralela(self):
        print("Iniciando multiplicacao paralela...")
        import threading
        
        resultado_par = [[0 for _ in range(self.n)] for _ in range(self.n)]
        threads = []
        
        def calcular_linha(i):
            for j in range(self.n):
                soma = 0
                for k in range(self.n):
                    soma += self.matriz_a[i][k] * self.matriz_b[k][j]
                resultado_par[i][j] = soma
            
        inicio = time.time()
        
        for i in range(self.n):
            t = threading.Thread(target=calcular_linha, args=(i,))
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
            
        fim = time.time()
        tempo_par = (fim - inicio) * 1000
        print(f"Tempo paralelo: {tempo_par:.2f} ms")
        return tempo_par
        
    def start_server(self):
        self.sock.bind(('localhost', 50251))
        self.sock.listen(5)
        print("Servidor matriz iniciado na porta 50251")
        
        tamanho = int(input("Digite o tamanho da matriz: "))
        self.gerar_matrizes(tamanho)
        
        tempo_seq = self.multiplicacao_sequencial()
        tempo_par = self.multiplicacao_paralela()
        
        num_workers = int(input("Quantos workers voce quer usar? "))
        print(f"Aguardando {num_workers} workers...")
        
        inicio_dist = time.time()
        
        for i in range(num_workers):
            client_sock, addr = self.sock.accept()
            print(f"Worker {i+1} conectado: {addr}")
            self.clients.append(client_sock)
            
        self.distribuir_trabalho()
        self.coletar_resultados()
        
        fim_dist = time.time()
        tempo_dist = (fim_dist - inicio_dist) * 1000
        
        print(f"Tempo distribuido: {tempo_dist:.2f} ms")
        print("Resultado final:")
        for linha in self.resultado:
            print(linha)
            
        with open('tempoAlgoritmos.txt', 'w') as f:
            f.write(f"Tamanho da matriz: {self.n}x{self.n}\n")
            f.write(f"Tempo sequencial: {tempo_seq:.2f} ms\n")
            f.write(f"Tempo paralelo: {tempo_par:.2f} ms\n")
            f.write(f"Tempo distribuido: {tempo_dist:.2f} ms\n")
            f.write(f"Clientes trabalhadores utilizados: {num_workers}\n")
            
        for client in self.clients:
            client.close()
            
    def distribuir_trabalho(self):
        linhas_por_worker = self.n // len(self.clients)
        linha_atual = 0
        
        for i, client in enumerate(self.clients):
            inicio_linha = linha_atual
            if i == len(self.clients) - 1:
                fim_linha = self.n
            else:
                fim_linha = linha_atual + linhas_por_worker
                
            dados = {
                'inicio': inicio_linha,
                'fim': fim_linha,
                'matriz_a': self.matriz_a[inicio_linha:fim_linha],
                'matriz_b': self.matriz_b,
                'worker_id': i
            }
            
            import pickle
            dados_serial = pickle.dumps(dados)
            client.send(dados_serial)
            
            linha_atual = fim_linha
            
    def coletar_resultados(self):
        import pickle
        
        for i, client in enumerate(self.clients):
            data = client.recv(4096)
            resultado_parcial = pickle.loads(data)
            
            inicio = resultado_parcial['inicio']
            linhas = resultado_parcial['resultado']
            
            for j, linha in enumerate(linhas):
                self.resultado[inicio + j] = linha

if __name__ == '__main__':
    server = MatrizServer()
    server.start_server()