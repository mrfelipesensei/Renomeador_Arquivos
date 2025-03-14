import os
import tkinter as tk
from tkinter import filedialog, messagebox

def listar_arquivos():
    pasta = entry_pasta.get().strip()

    if not pasta:
        messagebox.showwarning("Aviso","Selecione uma pasta primeiro!")
        return
    
    try:
        arquivos = os.listdir(pasta)
        if not arquivos:
            text_area.delete("1.0",tk.END)
            text_area.insert(tk.END, "A pasta está vaiza.")
        else:
            text_area.delete("1.0",tk.END)
            text_area.insert(tk.END, "Arquivos encontrados:\n")
            for arquivo in arquivos:
                text_area.insert(tk.END,f"{arquivo}\n")
    except FileNotFoundError:
        messagebox.showerror("Erro","Pasta não encontrada.")


def renomear_arquivos():
    pasta = entry_pasta.get().strip()
    novo_nome = entry_nome.get().strip()

    if not pasta or not novo_nome:
        messagebox.showwarning("Aviso","Preencha todos os campos")
        return
    

    arquivos = os.listdir(pasta)

    if not arquivos:
        messagebox.showerror("Erro","Nenhum arquivo encontrado na pasta.")
        return


    for i, arquivo in enumerate(arquivos, start=1):
        extesao = os.path.splitext(arquivo)[1] #Obtém a extensão do arquivo
        novo_nome_arquivo = f"{novo_nome}_{i}{extesao}"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome_arquivo)

        os.rename(caminho_antigo, caminho_novo)
        
    messagebox.showinfo("Suceso","Arquivos renomeados com sucesso!")
    listar_arquivos() #Atualiza a lista após renomeção

def selecionar_pasta():
    pasta_escolhida = filedialog.askdirectory()
    entry_pasta.delete(0, tk.END)
    entry_pasta.insert(0, pasta_escolhida)
    listar_arquivos() #Atualiza a lista ao selecionar pasta


#Criando a interface gráfica
root = tk.Tk()
root.title("Renomeador de Arquivos")

#Campo para selecionar pasta
tk.Label(root,text="Pasta:").grid(row=0,column=0)
entry_pasta = tk.Entry(root, width=40)
entry_pasta.grid(row=0,column=1)
tk.Button(root,text="Selecionar",command=selecionar_pasta).grid(row=0,column=2)

#Campo para o novo nome base
tk.Label(root,text="Novo Nome Base:").grid(row=1,column=0)
entry_nome = tk.Entry(root,width=40)
entry_nome.grid(row=1,column=1)

#Botão para listar aquivos
tk.Button(root,text="Atulizar Lista",command=listar_arquivos).grid(row=2,column=0,columnspan=3)

#Área de texto para exibir arquivos
text_area = tk.Text(root,height=10,width=50)
text_area.grid(row=3,column=0,columnspan=3)


#Botão para renomear
tk.Button(root, text="Renomear Arquivos",command=renomear_arquivos).grid(row=2,column=0,columnspan=3)

root.mainloop()