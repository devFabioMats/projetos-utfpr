#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import pickle

class MatrizClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def conectar_servidor(self):
        try:
            host = input("Digite o IP do servidor (ou enter para localhost): ")
            if host == "":
                host = "localhost"
            port = 50251
            
            print(f"Conectando em {host}:{port}...")
            self.sock.connect((host, port))
            print("Conectado ao servidor!")
            return True
        except:
            print("Erro ao conectar")
            return False
            
    def processar_trabalho(self):
        try:
            data = self.sock.recv(4096)
            trabalho = pickle.loads(data)
            
            worker_id = trabalho['worker_id']
            inicio = trabalho['inicio']
            fim = trabalho['fim']
            matriz_a = trabalho['matriz_a']
            matriz_b = trabalho['matriz_b']
            
            print(f"Worker {worker_id}: calculando linhas {inicio} a {fim-1}")
            
            resultado_linhas = []
            for i in range(len(matriz_a)):
                linha_resultado = []
                for j in range(len(matriz_b[0])):
                    soma = 0
                    for k in range(len(matriz_b)):
                        soma += matriz_a[i][k] * matriz_b[k][j]
                    linha_resultado.append(soma)
                resultado_linhas.append(linha_resultado)
                
            resultado = {
                'worker_id': worker_id,
                'inicio': inicio,
                'resultado': resultado_linhas
            }
            
            dados_retorno = pickle.dumps(resultado)
            self.sock.send(dados_retorno)
            
            print(f"Worker {worker_id}: trabalho concluido!")
            
        except Exception as e:
            print(f"Erro no processamento: {e}")
            
    def run(self):
        if self.conectar_servidor():
            self.processar_trabalho()
            self.sock.close()
            print("Desconectado do servidor")

if __name__ == '__main__':
    print("Cliente matriz iniciado")
    client = MatrizClient()
    client.run()