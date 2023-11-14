from tkinter import *

root = Tk()
root.title("CALCULADORA DE INTEIROS")
root.geometry("408x355")
root.minsize(408, 355)
root.maxsize(408, 355)

numero1 = ""
divisao = multiplicacao = adicao = subtracao = FALSE

root.configure(background="#282828")

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg="#FFFFFF", bg="#696969", font=("futura", 25, "bold"), justify=CENTER)

e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

# Funções de operações
def botaoClick(numero):
    e.insert(END, numero)
def botaoDivisao():
    global numero1
    global divisao
    divisao = True
    numero1 = e.get()
    e.delete(0, END)
def botaoMultiplicacao():
    global numero1
    global multiplicacao
    multiplicacao = True
    numero1 = e.get()
    e.delete(0, END)
def botaoSubtracao():
    global numero1
    global subtracao
    subtracao = True
    numero1 = e.get()
    e.delete(0, END)
def botaoAdicao():
    global numero1
    global adicao
    adicao = True
    numero1 = e.get()
    e.delete(0, END)
def botaoIgual():
    global subtracao, adicao, multiplicacao, divisao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
def botaoLimpar():
    e.delete(0, END)
divisao = Button(
    root,
    text="÷",
    padx=41,
    pady=20,
    command=botaoDivisao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#00008B",
    activebackground="#0000CD",
    relief=FLAT,
    font=("futura", 12, "bold")
)
divisao.grid(row=0, column=4)

# Primeira fileira
um = Button(
    root,
    text="1",
    padx=40,
    pady=20,
    command=lambda: botaoClick(1),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
um.grid(row=1, column=1)

dois = Button(
    root,
    text="2",
    padx=40,
    pady=20,
    command=lambda: botaoClick(2),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
dois.grid(row=1, column=2)

tres = Button(
    root,
    text="3",
    padx=40,
    pady=20,
    command=lambda: botaoClick(3),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
tres.grid(row=1, column=3)

multiplicacao = Button(
    root,
    text="×",
    padx=41,
    pady=20,
    command= botaoMultiplicacao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#00008B",
    activebackground="#0000CD",
    relief=FLAT,
    font=("futura", 12, "bold")
)
multiplicacao.grid(row=1, column=4)

# Segunda fileira
quatro = Button(
    root,
    text="4",
    padx=40,
    pady=20,
    command=lambda: botaoClick(4),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
quatro.grid(row=2, column=1)

cinco = Button(
    root,
    text="5",
    padx=40,
    pady=20,
    command=lambda: botaoClick(5),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
cinco.grid(row=2, column=2)

seis = Button(
    root,
    text="6",
    padx=40,
    pady=20,
    command=lambda: botaoClick(6),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
seis.grid(row=2, column=3)

subtracao = Button(
    root,
    text="–",
    padx= 41,
    pady= 20,
    command= botaoSubtracao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#00008B",
    activebackground="#0000CD",
    relief=FLAT,
    font=("futura", 12, "bold")
)
subtracao.grid(row=2, column=4)

# Terceira fileira
sete = Button(
    root,
    text="7",
    padx=40,
    pady=20,
    command=lambda: botaoClick(7),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
sete.grid(row=3, column=1)

oito = Button(
    root,
    text= "8",
    padx=40,
    pady=20,
    command=lambda: botaoClick(8),
    fg= "#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
oito.grid(row=3, column=2)

nove = Button(
    root,
    text="9",
    padx=40,
    pady=20,
    command=lambda: botaoClick(9),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
nove.grid(row=3, column=3)

adicao = Button(
    root,
    text="+",
    padx=41,
    pady=20,
    command= botaoAdicao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#00008B",
    activebackground="#0000CD",
    relief=FLAT,
    font=("futura", 12, "bold")
)
adicao.grid(row=3, column=4)

# Quarta fileira
zero = Button(
    root,
    text="0",
    padx=91,
    pady=20,
    command=lambda: botaoClick(0),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#0000CD",
    activebackground="#00008B",
    relief=FLAT,
    font=("futura", 12, "bold")
)
zero.grid(row=4, column=1, columnspan=2)

igual = Button(
    root,
    text="=",
    padx=40,
    pady=20,
    command=botaoIgual,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#00008B",
    activebackground="#0000CD",
    relief=FLAT,
    font=("futura", 12, "bold")
)
igual.grid(row=4, column=3)

limpa = Button(
    root,
    text="C",
    padx=40,
    pady=20,
    command=botaoLimpar,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#00008B",
    activebackground="#0000CD",
    relief=FLAT,
    font=("futura", 12, "bold")
)
limpa.grid(row=4, column=4)

root.mainloop()
