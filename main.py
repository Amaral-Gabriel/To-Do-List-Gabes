import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from funcoes import *

cinza = '#C0C0C0'
azul = '#87CEFA'
verde = '#008000'
branco = '#FFFAFA'


janela = Tk()
janela.title('To-Do List')
janela.geometry('800x600')
janela.configure(bg=branco)
janela.resizable(width=False,height=False)

frame_titulo = Frame(janela, width=800, height=70, bg=azul,relief='raised')
frame_titulo.grid(row=0,column=0,sticky=NW)
frame_adicionar = Frame(janela, width=800, height=50, bg=cinza,relief='raised')
frame_adicionar.grid(row=1,column=0,sticky=NW)

titulo = Label(frame_titulo, text="TO-DO LIST",font=("Ivy 30 bold"),fg=branco,bg=azul)
titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

adicionar = Button(frame_adicionar,command =lambda: abrir_nova_tarefa(janela), text="+ Adicionar nova tarefa",font=("Verdana",13),fg=branco,bg=cinza)
adicionar.place(relx=0.5,rely=0.5,anchor=CENTER)

espaco = Frame(janela, width=780,height=10,bg=branco)
espaco.grid(row=2,column=0)

tarefas = Frame(janela, width=800,height=600,bg=branco)
tarefas.grid(row=3,column=0)

#Criar barra de rolagem

tarefa1 = Frame(tarefas, width=200,height=200,bg=azul)
tarefa1.grid(row=0,column=0,padx=10, pady=10)
titulo_tarefa = Label(tarefa1, text="Título da tarefa aqui.",font=("Ivy 14 bold"),bg=azul)
data_tarefa = Label(tarefa1, text="Prazo: 28/09/2024",font=("Ivy 10 bold"),bg=azul)
titulo_tarefa.place(relx=0.5, rely=0.3, anchor=CENTER)
data_tarefa.place(relx=0.5, rely=0.9, anchor=CENTER)
detalhes_tarefa = Button(tarefa1, text="Ver detalhes",font=("Verdana",11),bg=branco)
detalhes_tarefa.place(relx=0.5,rely=0.7,anchor=CENTER)


janela.mainloop()