import tkinter as tk
import sqlite3

#Styles
title_font="inter 14 bold"
font_color="black"
background_color="#eee"
label_font="Arial 10 bold"
label_width=20
label_height=2
label_back_color="#eee"
entry_width=23
entry_font="Arial 10"
entry_font_color="black"
entry_back_color="#fff"
entry_border=2
button_font="Arial 10 bold"
button_font_color="black"
button_back_color="white"
button_width=9

#criação do banco e coneção 
conection=sqlite3.connect('db_tabs.db')
cursor=conection.cursor()

#criação das tabelas 
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS tab_alunos
    (nome TEXT, matricula TEXT, email TEXT, cpf TEXT)
   
    '''
)
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS tab_disciplinas
    (nome TEXT, id TEXT)
   
    '''
)
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS tab_professores
    (nome TEXT, matricula TEXT, email TEXT, cpf TEXT)
   
    '''
)


#função para atualizar e exibir os dados
def update_alunos_list():
    alunos_listbox.delete(0, tk.END)
    cursor.execute("SELECT nome, matricula, email, cpf FROM tab_alunos")

    for row in cursor.fetchall():
        alunos_listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")

def update_disciplinas_list():
    disciplinas_listbox.delete(0, tk.END)
    cursor.execute("SELECT nome, id FROM tab_disciplinas")

    for row in cursor.fetchall():
        disciplinas_listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def update_professores_list():
    professores_listbox.delete(0, tk.END)
    cursor.execute("SELECT nome, matricula, email, cpf FROM tab_professores")

    for row in cursor.fetchall():
        professores_listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")



#Fechar as telas
def fechar_containers():
    container_adicionar_alunos.pack_forget()
    container_adicionar_disciplinas.pack_forget()
    container_adicionar_professores.pack_forget()
    container_exibir_alunos.pack_forget()
    container_exibir_disciplinas.pack_forget()
    container_exibir_professores.pack_forget()

#Entradas de dados BD
def handle_add_aluno():
    nome=aluno_name_entry.get()
    matricula=aluno_matricula_entry.get()
    email=aluno_email_entry.get()
    cpf=aluno_cpf_entry.get()
    cursor.execute("INSERT INTO tab_alunos VALUES(?,?,?,?)",(nome,matricula,email,cpf))
    conection.commit()
    aluno_name_entry.delete(0,tk.END)
    aluno_matricula_entry.delete(0,tk.END)
    aluno_email_entry.delete(0,tk.END)
    aluno_cpf_entry.delete(0,tk.END)
    update_alunos_list()

def handle_add_disciplina():
    nome=disciplina_name_entry.get()
    id=disciplina_id_entry.get()
    cursor.execute("INSERT INTO tab_disciplinas VALUES(?,?)",(nome,id,))
    conection.commit()
    disciplina_name_entry.delete(0,tk.END)
    disciplina_id_entry.delete(0,tk.END)
    update_disciplinas_list()

def handle_add_professor():
    nome=professor_name_entry.get()
    matricula=professor_matricula_entry.get()
    email=professor_email_entry.get()
    cpf=professor_cpf_entry.get()
    cursor.execute("INSERT INTO tab_professores VALUES(?,?,?,?)",(nome,matricula,email,cpf))
    conection.commit()
    professor_name_entry.delete(0,tk.END)
    professor_matricula_entry.delete(0,tk.END)
    professor_email_entry.delete(0,tk.END)
    professor_cpf_entry.delete(0,tk.END)
    update_professores_list()
    

#Exibição das Telas
def novo_aluno():
    fechar_containers()
    container_adicionar_alunos.pack(ipadx=20,ipady=20,padx=5,pady=5,fill='both',expand=True)
    global aluno_name_entry, aluno_matricula_entry, aluno_email_entry, aluno_cpf_entry

    #formulário novo aluno
    aluno_title_label=tk.Label(container_adicionar_alunos,text="Novo Aluno",font=title_font,foreground=font_color,background=label_back_color,width=label_width)
    aluno_title_label.grid(row=0,column=0)

    aluno_name_label=tk.Label(container_adicionar_alunos,text="Nome",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    aluno_name_label.grid(row=1,column=1)

    aluno_name_entry=tk.Entry(container_adicionar_alunos,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    aluno_name_entry.grid(row=2,column=1)

    aluno_matricula_label=tk.Label(container_adicionar_alunos,text="Matricula",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    aluno_matricula_label.grid(row=3,column=1)

    aluno_matricula_entry=tk.Entry(container_adicionar_alunos,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    aluno_matricula_entry.grid(row=4,column=1)

    aluno_email_label=tk.Label(container_adicionar_alunos,text="E-mail",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    aluno_email_label.grid(row=5,column=1)

    aluno_email_entry=tk.Entry(container_adicionar_alunos,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    aluno_email_entry.grid(row=6,column=1)

    aluno_cpf_label=tk.Label(container_adicionar_alunos,text="CPF",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    aluno_cpf_label.grid(row=7,column=1)

    aluno_cpf_entry=tk.Entry(container_adicionar_alunos,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    aluno_cpf_entry.grid(row=8,column=1)

    submit_frame=tk.Frame(container_adicionar_alunos,pady=15)
    submit_frame.grid(row=9,column=1)
    cancelar_button=tk.Button(submit_frame,text="cancelar",font=button_font,foreground=button_font_color,background=button_back_color,width=button_width,command=fechar_containers)
    cancelar_button.grid(row=0,column=0)

    confirmar_button=tk.Button(submit_frame,text="Adicionar",font=button_font,foreground=button_font_color,background=button_back_color,width=button_width,command=handle_add_aluno)
    confirmar_button.grid(row=0,column=1)


def novo_disciplina():
    fechar_containers()
    container_adicionar_disciplinas.pack(ipadx=20,ipady=20,padx=5,pady=5,fill='both',expand=True)
    global disciplina_name_entry, disciplina_id_entry

    #formulário nova disciplina
    disciplina_title_label=tk.Label(container_adicionar_disciplinas,text="Adicionar Disciplina",font=title_font,foreground=font_color,background=label_back_color,width=label_width)
    disciplina_title_label.grid(row=0,column=0)

    disciplina_name_label=tk.Label(container_adicionar_disciplinas,text="Nome",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    disciplina_name_label.grid(row=1,column=1)

    disciplina_name_entry=tk.Entry(container_adicionar_disciplinas,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    disciplina_name_entry.grid(row=2,column=1)

    disciplina_id_label=tk.Label(container_adicionar_disciplinas,text="ID",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    disciplina_id_label.grid(row=3,column=1)

    disciplina_id_entry=tk.Entry(container_adicionar_disciplinas,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    disciplina_id_entry.grid(row=4,column=1)

    submit_frame=tk.Frame(container_adicionar_disciplinas,pady=15)
    submit_frame.grid(row=9,column=1)
    cancelar_button=tk.Button(submit_frame,text="cancelar",font=button_font,foreground=button_font_color,background=button_back_color,width=button_width,command=fechar_containers)
    cancelar_button.grid(row=0,column=0)

    confirmar_button=tk.Button(submit_frame,text="Adicionar",font=button_font,foreground=button_font_color,background=button_back_color,width=button_width,command=handle_add_disciplina)
    confirmar_button.grid(row=0,column=1)

def novo_professor():
    fechar_containers()
    container_adicionar_professores.pack(ipadx=20,ipady=20,padx=5,pady=5,fill='both',expand=True)
    global professor_name_entry, professor_matricula_entry, professor_email_entry, professor_cpf_entry

    #formulário novo professor
    professor_title_label=tk.Label(container_adicionar_professores,text="Novo Professor",font=title_font,foreground=font_color,background=label_back_color,width=label_width)
    professor_title_label.grid(row=0,column=0)

    professor_name_label=tk.Label(container_adicionar_professores,text="Nome",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    professor_name_label.grid(row=1,column=1)

    professor_name_entry=tk.Entry(container_adicionar_professores,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    professor_name_entry.grid(row=2,column=1)

    professor_matricula_label=tk.Label(container_adicionar_professores,text="Matricula",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    professor_matricula_label.grid(row=3,column=1)

    professor_matricula_entry=tk.Entry(container_adicionar_professores,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    professor_matricula_entry.grid(row=4,column=1)

    professor_email_label=tk.Label(container_adicionar_professores,text="E-mail",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    professor_email_label.grid(row=5,column=1)

    professor_email_entry=tk.Entry(container_adicionar_professores,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    professor_email_entry.grid(row=6,column=1)

    professor_cpf_label=tk.Label(container_adicionar_professores,text="CPF",font=label_font,foreground=font_color,background=label_back_color,width=label_width,anchor='sw',height=label_height)
    professor_cpf_label.grid(row=7,column=1)

    professor_cpf_entry=tk.Entry(container_adicionar_professores,width=entry_width,background=entry_back_color,font=entry_font,foreground=entry_font_color,border=entry_border)
    professor_cpf_entry.grid(row=8,column=1)

    submit_frame=tk.Frame(container_adicionar_professores,pady=15)
    submit_frame.grid(row=9,column=1)
    cancelar_button=tk.Button(submit_frame,text="cancelar",font=button_font,foreground=button_font_color,background=button_back_color,width=button_width,command=fechar_containers)
    cancelar_button.grid(row=0,column=0)

    confirmar_button=tk.Button(submit_frame,text="Adicionar",font=button_font,foreground=button_font_color,background=button_back_color,width=button_width,command=handle_add_professor)
    confirmar_button.grid(row=0,column=1)

def exibir_alunos_list():
    fechar_containers()
    container_exibir_alunos.pack(ipadx=20,ipady=20,padx=5,pady=5,fill='both',expand=True)
    #listagem de professores
    header_1 = tk.Label(container_exibir_alunos, text="Nome-Matricula-email-cpf")
    header_1.grid(row=0, column=0)

    alunos_listbox.grid(row=1,column=0)
    update_alunos_list()
    
def exibir_disciplinas_list():
    fechar_containers()
    container_exibir_disciplinas.pack(ipadx=20,ipady=20,padx=5,pady=5,fill='both',expand=True)
    #listagem de professores
    header_1 = tk.Label(container_exibir_disciplinas, text="Nome-ID")
    header_1.grid(row=0, column=0)

    disciplinas_listbox.grid(row=1,column=0)
    update_disciplinas_list()

def exibir_professores_list():
    fechar_containers()
    container_exibir_professores.pack(ipadx=20,ipady=20,padx=5,pady=5,fill='both',expand=True)
    #listagem de professores
    header_1 = tk.Label(container_exibir_professores, text="Nome-Matricula-email-cpf")
    header_1.grid(row=0, column=0)

    professores_listbox.grid(row=1,column=0)
    update_professores_list()

#Criação da janela e centralização
window = tk.Tk()
window_width=600
window_heigth=600
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
pos_x=(screen_width//2)-(window_width//2)
pos_y=(screen_height//2)-(window_heigth//2)
window.geometry('{}x{}+{}+{}'.format(window_width,window_heigth,pos_x,pos_y))
window.title("Colegio Estadual")

#cirrando telas
container_adicionar_alunos=tk.Frame(window,background=background_color)
container_adicionar_disciplinas=tk.Frame(window,background=background_color)
container_adicionar_professores=tk.Frame(window,background=background_color)
container_exibir_alunos=tk.Frame(window,background=background_color)
container_exibir_disciplinas=tk.Frame(window,background=background_color)
container_exibir_professores=tk.Frame(window,background=background_color)

#variaveis globais
alunos_listbox = tk.Listbox(container_exibir_alunos,width=100)
disciplinas_listbox = tk.Listbox(container_exibir_disciplinas,width=100)
professores_listbox = tk.Listbox(container_exibir_professores,width=100)

#Menu superior
main_menu=tk.Menu(window)
window.config(menu=main_menu)
adicionar_menu=tk.Menu(main_menu,tearoff=0)

#Menu Adicionar
main_menu.add_cascade(label="Adicionar",menu=adicionar_menu)
adicionar_menu.add_command(label="Aluno",command=novo_aluno)
adicionar_menu.add_command(label="Disciplina", command=novo_disciplina)
adicionar_menu.add_command(label="Professor",command=novo_professor)

#Menu exibir
exibir_menu=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="Exibir",menu=exibir_menu)
exibir_menu.add_command(label="Aluno",command=exibir_alunos_list)
exibir_menu.add_command(label="Disciplina",command=exibir_disciplinas_list)
exibir_menu.add_command(label="Professor",command=exibir_professores_list)


#apresentação da janela
window.mainloop()
