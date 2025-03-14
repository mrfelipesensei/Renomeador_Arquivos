import os

def listar_arquivos(pasta):
    try:
        arquivos = os.listdir(pasta)
        print("\n Arquivos na pasta:")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i}.{arquivo}")
    except FileExistsError:
        print("Erro: Pasta não encontrada.")

#Teste: listar os arquivos da pasta atual
pasta = input("Digite o caminho da pasta: ")
listar_arquivos(pasta)