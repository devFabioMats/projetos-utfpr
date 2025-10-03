#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Chave e nonce do seu sistema
key = b'A\xe0 9.\xd6\x1cNY\xba\xf7\x08d\xa9To'
nonce = b'\x95\xa4\xad#\xceg\xbd\x02w\x8cf\x05'
aesgcm = AESGCM(key)
aad = b"autenticado"

def extrair_dados_wireshark(texto_wireshark):
    """
    Extrai dados criptografados de uma captura do Wireshark
    Aceita diferentes formatos de saída do Wireshark
    """
    import re
    
    # Remove quebras de linha e espaços extras
    texto_limpo = texto_wireshark.replace('\n', '').replace('\r', '')
    
    # Tenta encontrar padrões hexadecimais
    # Padrão 1: bytes separados por pontos (como no seu exemplo)
    padrao_pontos = re.findall(r'[\da-fA-F]{2}', texto_limpo)
    
    if padrao_pontos and len(padrao_pontos) > 10:  # Pelo menos alguns bytes
        hex_string = ''.join(padrao_pontos)
        return bytes.fromhex(hex_string)
    
    # Padrão 2: hex contínuo
    padrao_hex = re.search(r'([0-9a-fA-F]{20,})', texto_limpo)
    if padrao_hex:
        return bytes.fromhex(padrao_hex.group(1))
    
    return None

def descriptografar_exemplo():
    """Exemplo com as suas mensagens"""
    
    # Suas mensagens do Wireshark (como apareceram na sua pergunta)
    mensagens_raw = [
        ".....,.p.4g..L?..Q...>1.A\".......9T...b.P..vr.[.3.O.....7.\"",
        ".....,.p.4g..C2.....u0\n.\"..#.....2I...b.P...]./.....M.k!..u",
        ".....,.p.4g..L?..Q...22..A.,\n....)I...b.Q&P..r......g..s.",
        ".....,.p.4g..C2.....i.4..A.-.........ZU;.K25.A.1s"
    ]
    
    print("TENTANDO DESCRIPTOGRAFAR AS MENSAGENS CAPTURADAS:")
    print("=" * 50)
    
    for i, msg in enumerate(mensagens_raw, 1):
        print(f"\nMensagem {i}:")
        print(f"Raw: {repr(msg)}")
        
        # Converte para bytes (as mensagens já estão como bytes no Wireshark)
        try:
            # Remove caracteres não imprimíveis e converte para bytes
            dados_bytes = msg.encode('latin-1')  # Preserva bytes originais
            
            # Tenta descriptografar
            try:
                resultado = aesgcm.decrypt(nonce, dados_bytes, aad)
                print(f"Descriptografada: {resultado.decode('utf-8')}")
            except Exception as e:
                print(f"Erro na descriptografia: {e}")
                
        except Exception as e:
            print(f"Erro na conversão: {e}")

def descriptografar_interativo():
    """Modo interativo para descriptografar"""
    print("\n=== MODO INTERATIVO ===")
    print("Cole os dados hexadecimais do Wireshark")
    print("Formatos aceitos:")
    print("- Hex contínuo: 41424344...")
    print("- Hex com espaços: 41 42 43 44")
    print("- Formato Wireshark: mostrado no painel de bytes")
    print("Digite 'sair' para terminar\n")
    
    contador = 1
    while True:
        entrada = input(f"Dados da mensagem {contador}: ").strip()
        
        if entrada.lower() == 'sair':
            break
            
        if not entrada:
            continue
        
        try:
            # Tenta diferentes métodos de conversão
            dados_bytes = None
            
            # Método 1: hex direto
            try:
                hex_limpo = ''.join(c for c in entrada if c in '0123456789ABCDEFabcdef')
                if len(hex_limpo) % 2 == 0 and len(hex_limpo) > 0:
                    dados_bytes = bytes.fromhex(hex_limpo)
            except:
                pass
            
            # Método 2: usando a função de extração
            if dados_bytes is None:
                dados_bytes = extrair_dados_wireshark(entrada)
            
            # Método 3: como string direta (para debug)
            if dados_bytes is None:
                dados_bytes = entrada.encode('latin-1')
            
            if dados_bytes:
                try:
                    resultado = aesgcm.decrypt(nonce, dados_bytes, aad)
                    print(f"✓ Mensagem {contador}: {resultado.decode('utf-8')}\n")
                    contador += 1
                except Exception as e:
                    print(f"✗ Erro na descriptografia: {e}")
                    print(f"  Tamanho dos dados: {len(dados_bytes)} bytes")
                    print(f"  Primeiros bytes: {dados_bytes[:20].hex() if len(dados_bytes) > 20 else dados_bytes.hex()}\n")
            else:
                print("✗ Não foi possível converter os dados\n")
                
        except Exception as e:
            print(f"✗ Erro geral: {e}\n")

if __name__ == "__main__":
    print("=== DESCRIPTOGRAFADOR DE MENSAGENS AES-GCM ===")
    print("\nEscolha uma opção:")
    print("1 - Tentar descriptografar as mensagens que você mostrou")
    print("2 - Modo interativo (cole dados do Wireshark)")
    
    opcao = input("\nOpção (1 ou 2): ").strip()
    
    if opcao == "1":
        descriptografar_exemplo()
    elif opcao == "2":
        descriptografar_interativo()
    else:
        print("Opção inválida")
    
    input("\nPressione Enter para sair...")