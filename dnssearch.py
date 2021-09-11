#!/usr/bin/env python3
import sys
import dns.resolver

dominio = 'bancocn.com'
lista = 'dnsbrutedictionaryPTBR.txt'

try:
    arquivo = open(lista)
    linhas = arquivo.read().splitlines()
except Exception:
    print("Arquivo não encontrado")
    sys.exit(1)

for linha in linhas:
    subdominio = linha + '.' + dominio
    try:
        respostas = dns.resolver.resolve(subdominio, 'a')
        for resultado in respostas:
            print(subdominio, resultado)
    except Exception:
        pass

input('#')

