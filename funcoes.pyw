import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import main

def abrir_nova_tarefa(janela):
    global entrada_titulo
    global entrada_descricao
    global entrada_prazo
    global marcar_feito
    global formulario
    global var1

    var1 = BooleanVar()

    formulario = tk.Toplevel(janela)
    formulario.title("Nova tarefa")
    formulario.geometry('400x300')

    tk.Label(formulario, text="Título da Tarefa:").grid(row=0, column=0, padx=10, pady=10)
    entrada_titulo = tk.Entry(formulario,width=30)
    entrada_titulo.grid(row=0, column=1, padx=10, pady=10,sticky=NW)

    tk.Label(formulario, text="Descrição:").grid(row=1, column=0, padx=10, pady=10)
    entrada_descricao = tk.Text(formulario, width=30, height=5)
    entrada_descricao.grid(row=1, column=1, padx=10, pady=10,sticky=NW)

    tk.Label(formulario, text="Prazo:").grid(row=2, column=0, padx=10, pady=10)
    entrada_prazo = DateEntry(formulario,selectmode="day")
    entrada_prazo.grid(row=2, column=1, padx=10, pady=10,sticky=NW)
    # Colocar horas no prazo

    tk.Label(formulario, text="Iniciar como feito?").grid(row=3, column=0, padx=10, pady=10)
    marcar_feito = tk.Checkbutton(formulario,variable=var1)
    marcar_feito.grid(row=3,column=1, padx=10, pady=10,sticky=NW)

    salvar = Button(formulario, command=lambda:salvar_dados(janela), text="Salvar",font=("Verdana",11),bg='#FFFAFA',width=20)
    salvar.grid(row=4,column=1, padx=10, pady=10,sticky=SE)

    fechar = Button(formulario, command=formulario.destroy, text="Cancelar",font=("Verdana",11),bg='#FFFAFA')
    fechar.grid(row=4,column=0, padx=10, pady=10, sticky=S)

    
    

def salvar_dados(janela):
    
    titulo = entrada_titulo.get()
    descricao = entrada_descricao.get("1.0", tk.END)
    prazo = entrada_prazo.get()
    box = var1.get()
    #tarefa = {"title":titulo, "descricao":descricao, "prazo":prazo, "CheckBox":box}
    #print(tarefa)
    print(box)
    
    formulario.destroy()
    

def ver_detalhes(janela):
    detalhe = tk.Toplevel(janela)
    detalhe.title("Detalhes da tarefa")
    detalhe.geometry('400x400')

    editar = Button(detalhe, text="Editar",font=("Verdana",11),bg='#FFFAFA')
    editar.grid(row=4,column=1, padx=10, pady=10,sticky=SE)

    fechar = Button(detalhe, command=detalhe.destroy, text="Cancelar",font=("Verdana",11),bg='#FFFAFA')
    fechar.grid(row=4,column=0, padx=10, pady=10, sticky=S)