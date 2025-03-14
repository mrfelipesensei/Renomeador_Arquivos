import os

def listar_arquivos(pasta):
    try:
        arquivos = os.listdir(pasta)
        print("\n Arquivos na pasta:")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i}.{arquivo}")
            return arquivos
    except FileExistsError:
        print("Erro: Pasta não encontrada.")
        return []


def renomear_arquivos(pasta, novo_nome):
    arquivos = listar_arquivos(pasta)
    if not arquivos:
        return
    

    for i, arquivo in enumerate(arquivos, start=1):
        extesao = os.path.splitext(arquivo)[1] #Obtém a extensão do arquivo
        novo_nome_arquivo = f"{novo_nome}_{i}{extesao}"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome_arquivo)

        os.rename(caminho_antigo, caminho_novo)
        print(f"{arquivo} ➜ {novo_nome_arquivo}")

#Entrada do usuário
pasta = input("Digite o caminho da pasta: ")
novo_nome = input("Digite o novo nome base para os arquivos: ")

#Executa a renomeação
renomear_arquivos(pasta, novo_nome)