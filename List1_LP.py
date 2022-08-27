'''
===================================================================
1 - Crie uma função que receberá diversas alturas através de inputs 
(em algum loop) e retornará a média delas. Essa função deve ser pro-
tegida contra entrada de valores inválidos.
===================================================================
'''

def alturas():
    try:
        quant = int(input("Quantas alturas você deseja?: "))
        
        soma = 0
        contador = 0
        
        while contador < quant:
            altura = int(input("Digite uma altura (em cm): "))
            soma += altura
            contador += 1
            
        media = soma/quant
        print(f"A média é {media}")
    
    except (ValueError, NameError, ZeroDivisionError):
        print("Digite um inteiro positivo!")
        return alturas()

'''
===================================================================
2 - Crie uma função que receberá um path para um arquivo .txt, irá
abrí-o em modo read, e caso o arquivo não exista, irá criá-lo.
===================================================================
'''

def criar_arquivo(path):
    try:
        open(path, "r")
    except FileNotFoundError:
        open(path, "a")
        print("Arquivo não encontrado!")

criar_arquivo("arquivo.txt")

'''
===================================================================
3 - Crie uma função que receberá duas listas de números e retornará
uma nova lista que é uma soma das duas listas. 
Ela deve ser protegida contra entrada de valores inválidos e, caso
as listas sejam de tamanhos diferentes, deve ser retornado uma men-
sagem ao usuário.
Exemplo 1:
[1, 3, 4, 6]
[2, 8, 11, 1]
Output:
[3, 11, 15, 7]
Exemplo 2:
[1, 5]
[4, 2, 8]
Output:
"Tamanhos não compatíveis!"
===================================================================
'''

def soma_listas(lista1, lista2):
    lista = list()
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            try:
                lista.append(lista1[i] + lista2[i])
            except ValueError:
                ("Valores inválidos!")
        return lista
    else:
        print("Tamanhos não compatíveis!")

print(soma_listas([2,5,6], [6,2]))

'''
===================================================================
4 - Crie uma função que receberá uma lista de nomes e irá lançar
uma exceção caso algum nome seja inválido.
Um nome é inválido quando:
- Não for uma string
- Tiver números
- Tiver um dos seguintes caracteres: "!@#$%¨&*()_+=-{}[]|:;<>,.?/
O tipo de exceção lançada deve ser diferente para cada um dos três
tipos de nomes inválidos. (Use raise Exception())
===================================================================
'''

def nomes(lista_nomes):
    if not isinstance(lista_nomes, list):
        print(f"{lista_nomes} não é uma lista!")
    else:
        print(f"{lista_nomes} é uma lista!")
    for nome in lista_nomes:
            str_ing(nome)
            num(nome)
            caracteres(nome)

def str_ing(nome):
    if not isinstance(nome, str):
        raise ValueError
                
def num(nome):
    for i in nome:
        if i.isdigit():
            raise ValueError
        
def caracteres(nome):
    caracteres_es = '"!@#$%¨&*()_+=-{}[]|:;<>,.?/'
    for i in caracteres_es:
        if i in nome:
            raise ValueError   
             
'''
===================================================================
5 - Crie uma função fatorial para os números inteiros não negativos
retorne o fatorial do número (exemplo 4!=24, 1!=1). Para criar essa 
função não é permitido utilizar bibliotecas, apenas o python 
padrão. Proteja a função para qualquer tipo de dados que seja
diferente dos números inteiros não negativos (-5! = exceção).
===================================================================
'''

def fatorial(num):
    try:
        if num < 0: 
            print("Fatorial de número negativo não existe!")

        elif num == 0: 
            return 1
            
        else: 
            fator = 1
            while(num > 1): 
                fator *= num 
                num -= 1
            return fator
    except:
        print("Não é um número inteiro!")