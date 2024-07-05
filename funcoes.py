import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import main

def abrir_nova_tarefa(janela):
    formulario = tk.Toplevel(janela)
    formulario.title("Nova tarefa")
    formulario.geometry('400x400')

    tk.Label(formulario, text="Título da Tarefa:").grid(row=0, column=0, padx=10, pady=10)
    entrada_titulo = tk.Entry(formulario)
    entrada_titulo.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(formulario, text="Descrição:").grid(row=1, column=0, padx=10, pady=10)
    entrada_descricao = tk.Entry(formulario)
    entrada_descricao.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(formulario, text="Prazo:").grid(row=2, column=0, padx=10, pady=10)
    entrada_descricao = tk.Entry(formulario)
    entrada_descricao.grid(row=2, column=1, padx=10, pady=10)