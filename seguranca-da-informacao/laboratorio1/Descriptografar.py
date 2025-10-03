#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import binascii

# Mesma chave e nonce usados no Client.py e Server.py
key = b'A\xe0 9.\xd6\x1cNY\xba\xf7\x08d\xa9To'
nonce = b'\x95\xa4\xad#\xceg\xbd\x02w\x8cf\x05'
aesgcm = AESGCM(key)
aad = b"autenticado"

# Mensagens capturadas no Wireshark (você precisa extrair apenas os dados criptografados)
# Exemplo de como converter do Wireshark para bytes:
# No Wireshark, copie os dados como "hex dump" e remova os caracteres não-hex

mensagens_capturadas = [
    # Cole aqui os dados hexadecimais das mensagens capturadas
    # Exemplo: "414243..." (sem espaços ou outros caracteres)
]

def hex_to_bytes(hex_string):
    """Converte string hexadecimal para bytes"""
    # Remove espaços, pontos e outros caracteres não-hex
    hex_clean = ''.join(c for c in hex_string if c in '0123456789ABCDEFabcdef')
    return bytes.fromhex(hex_clean)

def descriptografar_mensagem(dados_criptografados):
    """Descriptografa uma mensagem usando AES-GCM"""
    try:
        # Converte hex para bytes se necessário
        if isinstance(dados_criptografados, str):
            dados_criptografados = hex_to_bytes(dados_criptografados)
        
        # Descriptografa
        mensagem_original = aesgcm.decrypt(nonce, dados_criptografados, aad)
        return mensagem_original.decode('utf-8')
    except Exception as e:
        return f"Erro ao descriptografar: {e}"

def descriptografar_do_wireshark():
    """Função interativa para descriptografar mensagens do Wireshark"""
    print("=== DESCRIPTOGRAFADOR DE MENSAGENS ===")
    print("Cole os dados hexadecimais capturados no Wireshark")
    print("Digite 'sair' para terminar")
    print()
    
    contador = 1
    while True:
        hex_input = input(f"Mensagem {contador} (hex): ").strip()
        
        if hex_input.lower() == 'sair':
            break
            
        if not hex_input:
            continue
            
        try:
            mensagem = descriptografar_mensagem(hex_input)
            print(f"Mensagem {contador} descriptografada: {mensagem}")
            print()
            contador += 1
        except Exception as e:
            print(f"Erro: {e}")
            print("Verifique se os dados estão no formato correto")
            print()

def descriptografar_mensagens_predefinidas():
    """Descriptografa mensagens já definidas no código"""
    print("=== MENSAGENS PRÉ-DEFINIDAS ===")
    
    for i, msg in enumerate(mensagens_capturadas, 1):
        resultado = descriptografar_mensagem(msg)
        print(f"Mensagem {i}: {resultado}")

if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Descriptografar interativamente (cole dados do Wireshark)")
    print("2 - Descriptografar mensagens pré-definidas")
    
    opcao = input("Opção (1 ou 2): ").strip()
    
    if opcao == "1":
        descriptografar_do_wireshark()
    elif opcao == "2":
        descriptografar_mensagens_predefinidas()
    else:
        print("Opção inválida")