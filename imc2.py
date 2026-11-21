import tkinter as tk 

def calcular():

    txt_peso = campo_peso.get()
    txt_altura = campo_altura.get()

    if txt_peso == "" or txt_altura == "":
        resultado.config(text="Preencha ambos os campos")
        return
    try:
        peso = float(txt_peso.replace(",","."))
        altura = float(txt_altura.replace(",","."))
    except ValueError:
        resultado.config(text="Digite somente numeros!")
        return
    if peso <= 0 or altura <= 0:
        resultado.config(text="Peso e altura devem ser maiores que 0!")
        return
    if altura > 3:
        resultado.config(text="A altura deve ser menor que 3!")
        return
    if peso >= 200:
        resultado.config(text="O peso deve ser realista, acima de 200\n já sabemos que não é normal.")
        return


    imc = peso / altura ** 2

    if imc < 18.5:
        mensagem = "Abaixo do peso"
    elif imc < 25:
        mensagem = "Peso normal"
    elif imc < 30:
        mensagem = "Sobrepeso"
    elif imc < 35:
        mensagem = "Obesidade grau I"
    elif imc < 40:
        mensagem = "Obesidade grau II"
    else:
        mensagem = "Obesidade grau III"

    resultado.config(text=f"Seu IMC é: {round(imc,2)}\n{mensagem}")


# O Script em si é em cima
# O visual é o de baixo

janela = tk.Tk()

janela.title("Calculadora IMC")
janela.geometry("350x320")

# Centralizar os elementos
conteudo = tk.Frame(janela)
conteudo.place(relx=0.5, rely=0.5, anchor="center")

# Peso
tk.Label(conteudo, text="Digita o seu peso (KG):",
         font=("Segoe UI", 10)).pack()

campo_peso = tk.Entry(conteudo)
campo_peso.pack(pady=5)

# Altura
tk.Label(conteudo, text="Digita a sua altura (M):",
         font=("Segoe UI", 10)).pack()

campo_altura = tk.Entry(conteudo)
campo_altura.pack(pady=5)

# Botão
botao = tk.Button(
    conteudo,
    text="Calcule",
    command=calcular,
    font=("Segoe UI", 11),
    bg="#2563EB",
    fg="white",
    relief="flat",
    bd=0,
    padx=20,
    pady=8,
    cursor="hand2"
)
botao.pack(pady=10)

# Resultado
resultado = tk.Label(
    conteudo,
    text="",
    font=("Segoe UI", 10)
)
resultado.pack(pady=5)

janela.mainloop()