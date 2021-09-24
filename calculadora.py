# Calculadora
def calcualdora():
    opcao = 1
    while opcao:
        print("="*24)
        print("-"*6,"Calculadora","-"*5)
        print("0. Desligar")
        print("-"*24)
        print("1. Ir para modo básico")
        print("-"*24)
        print("2. Ir para modo avançado")
        print("="*24)
        
        opcao = int(input("Opções: "))
        if (opcao == 1):
            funcoesBasicas()
        if (opcao == 2):
            funcoesAvancadas()


def funcoesBasicas():
    def soma():
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Soma: ",x+y)

    def subtracao():
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Subtracao: ",x-y)

    def multiplicacao():
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Multiplicacao: ",x*y)

    def divisao():
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Divisao: ",x/y)

    def potencia2():
        base = float(input("Primeiro numero: "))
        expoente = float(input("Segundo numero: "))
        print("potencia: ", base ** expoente)

    def raizQuadrada():
        x = int(input("Primeiro numero: "))
        print(x ** (1/2))

    opcao = 1

    while opcao:
        print("="*20)
        print("0. Voltar")
        print("-"*20)
        print("1. Somar")
        print("-"*20)
        print("2. Subtrair")
        print("-"*20)
        print("3. Multiplicação")
        print("-"*20)
        print("4. Divisão")
        print("-"*20)
        print("5. Porntecia de 2")
        print("-"*20)
        print("6. Raiz quadrada")
        print("="*20)

        opcao = int(input("Opção: "))

        if(opcao==1):
            soma()
        if(opcao==2):
            subtracao()
        if(opcao==3):
            multiplicacao()
        if(opcao==4):
            divisao()
        if (opcao==5):
            potencia2()
        if (opcao==6):
            raizQuadrada()

def funcoesAvancadas():
    
    def potencia():
        n = int(input("Digite o valor de n: "))
        e = int(input("Digite o valor de E: "))

        pot = 1
        i   = 0
        while i < e:
            pot = pot * n
            i   = i + 1
        print("O valor de %d elevado a %d eh %d" %(n, e, pot))


    def equacao2Grau():
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
        D = (b**2 - 4*a*c)
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)

        print('\nValor de x1: {0:.2f}'.format(x1))
        print('\nValor de x2: {0:.2f}'.format(x2))

    def fatorial():
        n = int(input('Digite um número: '))
        f = 1
        for x in range(1, n+1):
            f = f * x
        print('O fatorial de %d é %d' % (n, f))

    def raizN():
        n = float(input('Digite um número: '))
        raiz = n ** 0.5
        print(f'\nA raiz quadrada de {n} é {raiz}\n')


    opcao = 1

    while opcao:
        print("="*13)
        print("0. Voltar")
        print("-"*13)
        print("1. Potência")
        print("-"*13)
        print("2. Equacao2Grau")
        print("-"*13)
        print("3. Fatorial")
        print("-"*13)
        print("4. Raiz de N")
        print("="*13)
        
        opcao = int(input("Opção: "))

        if(opcao==1):
            potencia()
        if(opcao==2):
            equacao2Grau()
        if (opcao==3):
            fatorial()
        if (opcao==4):
            raizN()

calcualdora()



