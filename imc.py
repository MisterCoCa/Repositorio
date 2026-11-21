# cria uma calculadora de imc em piton 

while True:
    txt_peso = input("Digite o seu peso. (APENAS NÚMEROS) \n")
    txt_altura = input("Digita a sua altura. (APENAS NÚMEROS) \n")

    if txt_peso.lower() == "stela" and txt_altura.lower() == "stela":
        print("https://maristelaoliveira.github.io/Python-Logica/")
        quit()

    if not txt_peso.replace('.', '', 1).isdigit() or not txt_altura.replace('.', '', 1).isdigit():
        print("Somente números!")
        continue

    peso = float(txt_peso) 
    altura = float(txt_altura)

    if not txt_peso.isdigit() or txt_altura.isdigit():
        print("Apenas números.")

    altura2 = (altura * altura)
    altura_float = float(altura2)
    print("Altura ao quadrado: ",altura2)

    resultado = peso / altura2

    imc = print("Teu IMC é:", round(resultado,2))

    if resultado >= 40.0:
        print("Obeso Nível 3 - Vá se tratar logo, isso é extremamente preocupante.")
        obeso = []

    elif resultado >= 35.0:
        print("Obeso Nível 2 - Vá se tratar, isso ta bem preocupante.")

    elif resultado >= 30.0:
        print("Obeso Níve 1 - Vá se tratar, isso ta començando a ficar preocupante.")

    elif resultado >= 25.0:
        print("Sobrepeso - Procure melhorar para evitas problemas futuros.")

    elif resultado >= 18.5:
        print("Padrão - Ta de boa.")

    else:
        print("Magro - Deve ir atrás de especialistas, isso pode ficar sério.") 

    quiz = input("Você quer refazer o teste? (s OU n) \n")
    if quiz.lower() == "n":
        print("Ok.")
        quit()
    elif quiz.lower() == "s":
        print("Ok!")
        continue

