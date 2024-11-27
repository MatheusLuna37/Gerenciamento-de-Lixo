from leitura_dados import ler_dados_do_arquivo
from Grafo import Grafo
from Ponto import Ponto
from Caminhao import Caminhao
from Carrocinha import Carrocinha

# Caminho do arquivo de entrada
arquivo_entrada = "entrada.txt"

# Lendo os dados do arquivo
dados = ler_dados_do_arquivo(arquivo_entrada)

if dados:
    adjacencias, aterro, zoonoses = dados
    bairro = Grafo(adjacencias, aterro, zoonoses)

    # Exibindo os dados carregados do arquivo
    print("Adjacências:", [{ponto.id: [(p.id, custo) for p, custo in adjacencias[ponto]]} for ponto in adjacencias])
    print("Aterro sanitário:", bairro.aterro.id)
    print("Centro de zoonoses:", bairro.zoonoses.id)

    
