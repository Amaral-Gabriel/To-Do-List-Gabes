import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
#import main
import json

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

global tarefas
global janela

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
tarefas_frame = Frame(janela, width=800,height=600,bg=branco)
tarefas_frame.grid(row=3,column=0)

###############################################################################################

tarefas =[]
tarefa_cont = 0

def abrir_nova_tarefa(janela): # Abre a nova aba que será responsável por fazer o input dos dados
    global entrada_titulo
    global entrada_descricao
    global entrada_prazo
    global marcar_feito
    global formulario
    global var1
    global titulo_var

    # Define algumas variaveis que serão usadas depois
    var1 = BooleanVar()
    titulo_var = StringVar()

    # Janela que recebe os dados
    formulario = tk.Toplevel(janela)
    formulario.title("Nova tarefa")
    formulario.geometry('400x300')

    # Recebe o título
    tk.Label(formulario, text="Título da Tarefa:").grid(row=0, column=0, padx=10, pady=10)
    entrada_titulo = tk.Entry(formulario,width=30,textvariable=titulo_var,font=("Verdana",10))
    entrada_titulo.grid(row=0, column=1, padx=10, pady=10,sticky=NW)

    # Recebe a descrição
    tk.Label(formulario, text="Descrição:").grid(row=1, column=0, padx=10, pady=10)
    entrada_descricao = tk.Text(formulario, width=30, height=5,font=("Verdana",10))
    entrada_descricao.grid(row=1, column=1, padx=10, pady=10,sticky=NW)

    # Recebe o prazo
    tk.Label(formulario, text="Prazo:").grid(row=2, column=0, padx=10, pady=10)
    entrada_prazo = DateEntry(formulario,selectmode="day",date_pattern='dd/MM/yyyy')
    entrada_prazo.grid(row=2, column=1, padx=10, pady=10,sticky=NW)
    ### Colocar horas no prazo

    # Checa se será iniciado como concluído
    tk.Label(formulario, text="Iniciar como feito?").grid(row=3, column=0, padx=10, pady=10)
    marcar_feito = tk.Checkbutton(formulario,variable=var1)
    marcar_feito.grid(row=3,column=1, padx=10, pady=10,sticky=NW)

    # Botão salvar
    salvar = Button(formulario, command=lambda:salvar_dados(janela), text="Salvar",font=("Verdana",11),bg='#FFFAFA',width=20)
    salvar.grid(row=4,column=1, padx=10, pady=10,sticky=SE)

    # Botão fechar
    fechar = Button(formulario, command=formulario.destroy, text="Cancelar",font=("Verdana",11),bg='#FFFAFA')
    fechar.grid(row=4,column=0, padx=10, pady=10, sticky=S)

def salvar_dados(janela): # Coleta os dados da 'função abrir_nova_tarefa()', e armazena em uma lista
    global tarefa
    global titulo
    global prazo
    global descricao
    global box

    # Adicionar tela de erro caso o titulo esteja vazio
    if not titulo_var.get().strip():
        erro = tk.Toplevel(janela)
        erro.title("Erro")
        erro.geometry('300x200')
        erro_label = tk.Label(erro, text="O título não pode estar vazio!", font=("Verdana", 10), fg="red")
        erro_label.pack(pady=20)
        erro_button = tk.Button(erro, text="Fechar", command=erro.destroy)
        erro_button.pack(pady=10)
    else:
        titulo = titulo_var.get()
        descricao = entrada_descricao.get("1.0", tk.END)
        prazo = entrada_prazo.get()
        box = var1.get()
        tarefa = {"title":titulo, "descricao":descricao, "prazo":prazo, "CheckBox":box}
        
        # Adiciona a tarefa
        adicionar_tarefa(janela)
        tarefas.append(tarefa)
        salvar_tarefas()
        adicionar_tarefa(tarefa)

        # Fecha a janela
        formulario.destroy()

def salvar_tarefas():
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f, indent=4)
    


def carregar_tarefas():
    global tarefas
    try:
        with open('tarefas.json', 'r') as f:
            tarefas = json.load(f)
            for tarefa in tarefas:
                adicionar_tarefa(tarefa)
    except FileNotFoundError:
        tarefas = []


def adicionar_tarefa(tarefa): # Função responsável por adicionar frames contendo os dados das tarefas e mostrar no frame 'tarefas'
    global tarefa_cont
    tarefa_cont += 1

    row = tarefa_cont // 4
    column = tarefa_cont % 4

    ### Criar o sistema que irá permitir a criação de várias tarefas
    frame_tarefa = Frame(tarefas_frame, width=180,height=200,bg=azul)
    frame_tarefa.grid(row=row,column=column,padx=10, pady=10)
    titulo_tarefa = Label(frame_tarefa, text=titulo[:15],font=("Ivy 14 bold"),bg=azul)
    data_tarefa = Label(frame_tarefa, text=prazo,font=("Ivy 10 bold"),bg=azul)
    titulo_tarefa.place(relx=0.5, rely=0.3, anchor=CENTER)
    data_tarefa.place(relx=0.5, rely=0.9, anchor=CENTER)
    detalhes_tarefa = Button(frame_tarefa, command=lambda:ver_detalhes(tarefa), text="Ver detalhes",font=("Verdana",11),bg=branco)
    detalhes_tarefa.place(relx=0.5,rely=0.7,anchor=CENTER)
    for i in range(3):
        tarefas_frame.grid_columnconfigure(i, weight=1, minsize=200)
    tarefas_frame.grid_rowconfigure(row, weight=1, minsize=200)
    
def ver_detalhes(tarefa): # Abre a janela que permite o usuario vizualizar todos os dados da tarefa
    global feito_detalhe
    global editar
    global detalhe
    detalhe = tk.Toplevel(janela)
    detalhe.title("Detalhes da tarefa")
    detalhe.geometry('400x400')
    detalhe.grid_columnconfigure(0,weight=1)

    # Frame do título
    titulo_detalhe = Label(detalhe,text=titulo,bg=cinza_claro,font=("Ivy 10 bold"),anchor=CENTER)
    titulo_detalhe.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

    # Frame da descrição
    frame_descricao = Frame(detalhe,bg=azul)
    frame_descricao.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=W)

    # Cria o scrollbar para o frame da descrição
    scrollbar = Scrollbar(frame_descricao)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    ### Configurar se o scrollbar deve aparecer dependendo da quantidade de letras

    descricao_detalhe = Text(frame_descricao, height=10, bg=branco, font=("Ivy 10 bold"), wrap=tk.WORD, yscrollcommand=scrollbar.set)
    descricao_detalhe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    descricao_detalhe.insert(END, descricao)
    descricao_detalhe.config(state=tk.DISABLED)

    scrollbar.config(command=descricao_detalhe.yview)

    # Frame prazo
    prazo_detalhe = Label(detalhe,text="Prazo: "+prazo,bg=cinza_claro,font=("Ivy 10 bold"),anchor=CENTER)
    prazo_detalhe.grid(row=2,column=0,columnspan=3, padx=10, pady=10)

    # Verifica se a tarefa está concluida ou pendente
    if box == True:
        feito_detalhe = Label(detalhe,text="Concluido",bg=cinza_claro,font=("Ivy 10 bold"),anchor=CENTER)
        feito_detalhe.grid(row=3,column=0,columnspan=3, padx=10, pady=10)
    else:
        feito_detalhe = Label(detalhe,text="Pendente",bg=cinza_claro,font=("Ivy 10 bold"),anchor=CENTER)
        feito_detalhe.grid(row=3,column=0,columnspan=3, padx=10, pady=10)

    # Botão editar
    editar = Button(detalhe, command=lambda:editar_tarefa(janela), text="Editar",font=("Verdana",11),bg='#FFFAFA')
    editar.grid(row=4,column=2, padx=10, pady=10)

    ### Criar função de editar tarefa
    def editar_tarefa(janela): # Abre a nova aba que será responsável por fazer o input dos dados
        global entrada_titulo
        global entrada_descricao
        global entrada_prazo
        global marcar_feito
        global formulario
        global var1
        global titulo_var

        # Define algumas variaveis que serão usadas depois
        var1 = BooleanVar()
        titulo_var = StringVar()

        # Janela que recebe os dados
        formulario = tk.Toplevel(detalhe)
        formulario.title("Editar tarefa")
        formulario.geometry('400x300')

        # Recebe o título
        tk.Label(formulario, text="Título da Tarefa:").grid(row=0, column=0, padx=10, pady=10)
        entrada_titulo = tk.Entry(formulario,width=30,textvariable=titulo_var,font=("Verdana",10))
        entrada_titulo.grid(row=0, column=1, padx=10, pady=10,sticky=NW)
        entrada_titulo.insert(0,titulo)

        # Recebe a descrição
        tk.Label(formulario, text="Descrição:").grid(row=1, column=0, padx=10, pady=10)
        entrada_descricao = tk.Text(formulario, width=30, height=5,font=("Verdana",10))
        entrada_descricao.grid(row=1, column=1, padx=10, pady=10,sticky=NW)
        entrada_descricao.insert("1.0",descricao)

        # Recebe o prazo
        tk.Label(formulario, text="Prazo:").grid(row=2, column=0, padx=10, pady=10)
        entrada_prazo = DateEntry(formulario,selectmode="day",date_pattern='dd/MM/yyyy')
        entrada_prazo.grid(row=2, column=1, padx=10, pady=10,sticky=NW)
        ### Colocar horas no prazo

        # Checa se será marcado como concluído
        tk.Label(formulario, text="Marcar como feito?").grid(row=3, column=0, padx=10, pady=10)
        if box:
            var1 = tk.IntVar(value=1)
        else:
            var1 = tk.IntVar(value=0)
        marcar_feito = tk.Checkbutton(formulario,variable=var1)
        marcar_feito.grid(row=3,column=1, padx=10, pady=10,sticky=NW)

        # Botão salvar
        salvar = Button(formulario, command=lambda:salvar_e_fechar(janela), text="Salvar",font=("Verdana",11),bg='#FFFAFA',width=20)
        salvar.grid(row=4,column=1, padx=10, pady=10,sticky=SE)

        # Botão fechar
        fechar = Button(formulario, command=lambda:fechar_janela(detalhe), text="Cancelar",font=("Verdana",11),bg='#FFFAFA')
        fechar.grid(row=4,column=0, padx=10, pady=10, sticky=S)

    def salvar_e_fechar(detalhe):
            # Adicionar tela de erro caso o titulo esteja vazio
        if not titulo_var.get().strip():
            erro = tk.Toplevel(janela)
            erro.title("Erro")
            erro.geometry('300x200')
            erro_label = tk.Label(erro, text="O título não pode estar vazio!", font=("Verdana", 10), fg="red")
            erro_label.pack(pady=20)
            erro_button = tk.Button(erro, text="Fechar", command=erro.destroy)
            erro_button.pack(pady=10)
        else:
            salvar_dados(janela)
            fechar_janela(janela)

    # Fecha a janela de detalhes e editar
    def fechar_janela(janela):
        formulario.destroy()
        detalhe.destroy()

    if not box:
        editar = Button(detalhe,command=lambda:concluir(detalhe), text="Concluir",font=("Verdana",11),bg='#FFFAFA')
        editar.grid(row=4, column=1, padx=10, pady=10)

    # Botão fechar
    fechar = Button(detalhe, command=detalhe.destroy, text="Voltar",font=("Verdana",11),bg='#FFFAFA')
    fechar.grid(row=4,column=0, padx=10, pady=10,sticky=W)


# Cria botao para alterar o concluido
def concluir(detalhe):
    global box
    feito_detalhe.config(text="Concluido")
    editar.destroy()
    box = True
    tarefa = {"title":titulo, "descricao":descricao, "prazo":prazo, "CheckBox":box}


janela.mainloop()