import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import main

cinza = '#C0C0C0'
azul = '#87CEFA'
verde = '#008000'
branco = '#FFFAFA'

def abrir_nova_tarefa(janela):
    global entrada_titulo
    global entrada_descricao
    global entrada_prazo
    global marcar_feito
    global formulario
    global var1
    global titulo_var

    var1 = BooleanVar()
    titulo_var = StringVar()

    formulario = tk.Toplevel(janela)
    formulario.title("Nova tarefa")
    formulario.geometry('400x300')

    tk.Label(formulario, text="Título da Tarefa:").grid(row=0, column=0, padx=10, pady=10)
    entrada_titulo = tk.Entry(formulario,width=30,textvariable=titulo_var)
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
    global tarefa
    global titulo
    global prazo

    titulo = titulo_var.get()
    descricao = entrada_descricao.get("1.0", tk.END)
    prazo = entrada_prazo.get()
    box = var1.get()
    tarefa = {"title":titulo, "descricao":descricao, "prazo":prazo, "CheckBox":box}
    print(tarefa)

    
    adicionar_tarefa(janela)
    formulario.destroy()

def adicionar_tarefa(janela):
    tarefa = Frame(janela, width=200,height=200,bg=azul)
    tarefa.grid(row=3,column=0,padx=10, pady=10)
    titulo_tarefa = Label(tarefa, text=titulo[:16],font=("Ivy 14 bold"),bg=azul)
    data_tarefa = Label(tarefa, text=prazo,font=("Ivy 10 bold"),bg=azul)
    titulo_tarefa.place(relx=0.5, rely=0.3, anchor=CENTER)
    data_tarefa.place(relx=0.5, rely=0.9, anchor=CENTER)
    detalhes_tarefa = Button(tarefa, command=lambda:ver_detalhes(tarefa), text="Ver detalhes",font=("Verdana",11),bg=branco)
    detalhes_tarefa.place(relx=0.5,rely=0.7,anchor=CENTER)
    

def ver_detalhes(janela):
    detalhe = tk.Toplevel(janela)
    detalhe.title("Detalhes da tarefa")
    detalhe.geometry('400x400')

    editar = Button(detalhe, text="Editar",font=("Verdana",11),bg='#FFFAFA')
    editar.grid(row=4,column=1, padx=10, pady=10,sticky=SE)

    fechar = Button(detalhe, command=detalhe.destroy, text="Cancelar",font=("Verdana",11),bg='#FFFAFA')
    fechar.grid(row=4,column=0, padx=10, pady=10, sticky=S)