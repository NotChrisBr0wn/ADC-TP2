import pickle

from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas

from veiculos import nome_ficheiro_lista_de_veiculos



# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_ficheiros*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro io_ficheiros.py existente, deve apagar
# todos os outros ficheiros io_ficheiros-*.py, e inclusive estes comentários

# ...
def carrega_as_listas_dos_ficheiros():
    """TODO: documentação"""

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)

    return  lista_de_veiculos, lista_de_clientes, lista_de_faturas
