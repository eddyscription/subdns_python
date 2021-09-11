# subdns_python
Programa simples em Python para procurar subdomínios em um site, anexados estão o script e um dicionário que pode ser trocado por qualquer outro relativo ao mesmo objetivo. 
A saída de dados será do subdomínio e o IPv4 referente ao mesmo:



#!/usr/bin/env python3
import sys
import dns.resolver

dominio = 'bancocn.com' #dominio de exemplo
lista = 'dnsbrutedictionaryPTBR.txt'

try: #ira ler linha por linha do dicionario
    arquivo = open(lista)
    linhas = arquivo.read().splitlines()
except Exception:
    print("Arquivo não encontrado")
    sys.exit(1)

for linha in linhas: #ira resolver os subdns
    subdominio = linha + '.' + dominio
    try:
        respostas = dns.resolver.resolve(subdominio, 'a')
        for resultado in respostas:
            print(subdominio, resultado)
    except Exception:
        pass

input('#')

