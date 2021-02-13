# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:44:38 2021

@author: User
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

from cryptography.fernet import Fernet

        
# FUNCION PARA DESENCRIPTAR ARCHIVO
def desencript(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(nom_archivo, 'wb') as file:
            file.write(decrypted_data)

def clave(s, lista = list(), base = ''):
    i =0
    if len (s) == 0:
         lista.append('MZygpewJsCpR' + base)
         i +=1
         
    else:
        for i in range(len(s)):
            clave(s[:i]+s[i+1:], lista, base+s[i])   

lista = []
clave('abcd', lista)

# FUNCION PARA CARGAR LA CLAVE
def cargar_clave():
    return open('klave.key','rb').read()

# CARGAMOS CLAVE
clave = cargar_clave()

# ARCHIVO A ENCRIPTAR
nom_archivo = 'archivoEncriptado.txt'

# DESENCRIPTAR ARCHIVO
desencript(nom_archivo, clave)


# for i in range(len(lista)):
#     # f= Fernet(lista[i])
#     desencript('archivoEncriptado.txt', lista[0])
#     print(i)
    