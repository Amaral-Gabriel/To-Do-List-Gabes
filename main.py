import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


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

adicionar = Button(frame_adicionar, text="+ Adicionar nova tarefa",font=("Verdana",13),fg=branco,bg=cinza)
adicionar.place(relx=0.5,rely=0.5,anchor=CENTER)

espaco = Frame(janela, width=780,height=10,bg=branco)
espaco.grid(row=2,column=0)

tarefas = Frame(janela, width=800,height=600,bg=branco)
tarefas.grid(row=3,column=0)

#Criar barra de rolagem

tarefa1 = Frame(tarefas, width=200,height=200,bg=verde)
tarefa1.grid(row=0,column=0,padx=10, pady=10)

tarefa2 = Frame(tarefas, width=200,height=200,bg=verde)
tarefa2.grid(row=0,column=1,padx=10, pady=10)

tarefa3 = Frame(tarefas, width=200,height=200,bg=verde)
tarefa3.grid(row=0,column=2,padx=10, pady=10)

tarefa4 = Frame(tarefas, width=200,height=200,bg=verde)
tarefa4.grid(row=1,column=0,padx=10, pady=10)

tarefa5 = Frame(tarefas, width=200,height=200,bg=verde)
tarefa5.grid(row=2,column=1,padx=10, pady=10)

tarefa6 = Frame(tarefas, width=200,height=200,bg=verde)
tarefa6.grid(row=3,column=1,padx=10, pady=10)

janela.mainloop()