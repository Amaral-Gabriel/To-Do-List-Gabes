import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from funcoes import *

global tarefas
global janela

# Comentários marcados com: ###, são lembretes de funções que devem ser adicionadas

# Definição de cores
cinza = '#C0C0C0'
azul = '#87CEFA'
verde = '#008000'
cinza_claro = "#F0F0F0" # Usado para fundos ou elementos de destaque
cinza_medio = "#C0C0C0" # Usado para elementos secundários
cinza_escuro = "#808080" # Usado para texto ou bordas
azul_claro = "#87CEFA" # Usado para elementos principais
azul_escuro = "#4682B4" # Usado para texto ou elementos de destaque
branco = "#FFFFFF" # Usado para fundos ou texto

# Janela principal
janela = Tk()
janela.title('To-Do List')
janela.geometry('800x600')
janela.configure(bg=branco)
janela.resizable(width=False,height=False) # Não permite o ajuste do tamanho da janela

# Título do programa
frame_titulo = Frame(janela, width=800, height=70, bg=azul,relief='raised')
frame_titulo.grid(row=0,column=0,sticky=NW)
frame_adicionar = Frame(janela, width=800, height=50, bg=cinza,relief='raised')
frame_adicionar.grid(row=1,column=0,sticky=NW)

titulo = Label(frame_titulo, text="TO-DO LIST",font=("Ivy 30 bold"),fg=branco,bg=azul)
titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

# Navbar com o botão adicionar
adicionar = Button(frame_adicionar,command =lambda: abrir_nova_tarefa(janela), text="+ Adicionar nova tarefa",font=("Verdana",13),fg=branco,bg=cinza)
adicionar.place(relx=0.5,rely=0.5,anchor=CENTER)

# Gera um espaço entres os frames
espaco = Frame(janela, width=780,height=10,bg=branco)
espaco.grid(row=2,column=0)

# Frame reservado para mostrar as tarefas
tarefas = Frame(janela, width=800,height=600,bg=branco)
tarefas.grid(row=3,column=0)

###Criar barra de rolagem



janela.mainloop()