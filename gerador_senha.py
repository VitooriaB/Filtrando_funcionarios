#Gerador de senhas seguras
#Altere as quantidade conforme o seu gosto 
# NUNCA USE RANDOM PARA GERADOR DE SENHA. 

import secrets
from string import ascii_letters, digits


#Tipos de simbolos
symbols = '!#$%&()*+><^~@-_çÇ`/|ªº¿'
alfabeto = ascii_letters + digits + symbols

#Quantidade de letras,simbolos e numeros 
qtd_letras = 10
qtd_digitos = 4
qtd_simbolos = 2

tamanho_senha = qtd_simbolos + qtd_digitos + qtd_letras
while True:
    password = ''.join(secrets.choice(alfabeto) for _ in range(tamanho_senha))
    if (sum(c.isalpha() for c in password) == qtd_letras
            and sum(c in symbols for c in password) == qtd_simbolos
            and sum(c.isdigit() for c in password) == qtd_digitos): 
        break # deu certo, sai do while

print(password)

