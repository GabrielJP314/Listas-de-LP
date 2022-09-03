import numpy as np
import numpy.random as npr
from functools import reduce

'''
===================================================================
1 - Crie uma função usando numpy que caso receba uma matriz 
bidimensional numpy retorna um vetor unidimensional. Se a entrada é
um vetor unidimensional retorne uma matriz diagonal com os 
elementos do vetor. Caso contrário levante uma exceção ValueError.
===================================================================
''' 

def diagonalEspecial(array):
    if isinstance(array, np.ndarray):
        if array.ndim == 2:
            quant_elementos = np.size(array)
            array_1d = array.reshape(quant_elementos)
            return array_1d
        elif array.ndim == 1:
            return np.diag(array)
        else:
            raise ValueError
    else:
        raise ValueError

print(diagonalEspecial(np.array([[1,2,3],[1,2,3]])))

'''
===================================================================
2 - Crie uma função para simular o jogo pedra papel tesoura usando 
números aleatórios do numpy.
- Suponha que tirar pedra, papel ou tesoura possui a mesma 
probabilidade de acontecer.
- A entrada corresponde ao número de vezes que o experimento deve
acontecer.
- A função deve retornar um dicionário com a quantidade de vezes
que cada evento aconteceu (ex: {'papel':1,'pedra':3,'tesoura':2})
===================================================================
'''

def jokenpo(n):
    npr.seed(n)
    sequencia = npr.randint(1,4,n)
    pedra = 0
    papel = 0
    tesoura = 0
    dicio = {}
    for i in sequencia:
        if i == 1:
            pedra += 1
        elif i == 2:
            papel += 1
        else:
            tesoura += 1
       
    dicio['pedra'] = pedra
    dicio['papel'] = papel
    dicio['tesoura'] = tesoura
       
    return dicio

print(jokenpo(20))

'''
===================================================================
3 - Crie uma função para expandir uma matriz numpy. Dada uma matriz
A de dimensão mxn, retorne A com dimensão kxk onde k = max(m,n).
Completando com zeros até que A possua a dimensão kxk. 
===================================================================
'''

def expandir(array):
    if isinstance(array, np.ndarray):
        tam = np.shape(array)
        if tam[0] > tam[1]:
            return np.hstack((array, np.zeros((tam[0], tam[0]-tam[1]))))
        elif tam[0] < tam[1]:
            return np.vstack((array, np.zeros((tam[1]-tam[0], tam[1]))))
        else:
            raise ValueError
    else:
        raise ValueError ("Não é da classe ndarray!")
        
print(expandir(np.array([[1,0,0]])))

'''
===================================================================
4 - Crie uma função numpy que dada uma matriz A de dimensão mxn. 
Retorne um vetor coluna mx1 onde cada entrada i 
corresponde ao menor valor da linha i.
===================================================================
'''

def minimos(A):
    transposta = np.sort(A).T
    print(transposta[0])
    
minimos(np.array([[3,7,1],[6,1,3],[9,3,5],[7,6,4]]))        

'''
===================================================================
5 - Sabemos que uma multiplicação de matrizes não é comutativa. 
Mas, em alguns casos é possível verificar que A*B = B*A. Crie uma 
função que dada duas matrizes ela retorna verdadeiro se A*B=B*A e
retorna falso caso contrário. Observe que quando A e B não são 
matrizes quadradas a função deve retornar falso, independente do 
tamanho de A e B.
===================================================================
'''

def AB_igual_BA(A,B):
    try:
        A.shape[1]
        B.shape[1]
        if np.array_equal(np.dot(A, B), np.dot(B, A)):
            return True
        else:
            return False
    except:
        return False

A = np.array([[1,-2],[0,3]])
B = np.array([[1,-1], [0,2]])
print(AB_igual_BA(A,B))

'''
===================================================================
6 - Crie uma função que recebe uma lista de vetores numpy, retorne 
o vetor que possuiu a menor norma vetorial. 
Desafio opcional: tente resolver essa questão com uma só linha de 
código, recomendo utilizar map e função lambda. Confira a seguir:
https://medium.com/horadecodar/express%C3%B5es-lambda-em-python-com-map-reduce-e-filter-a391368ae886
https://cs.stanford.edu/people/nick/py/python-map-lambda.html
===================================================================
'''

def menorNorma(l):
    return reduce(lambda x,y: x if(np.linalg.norm(x)<np.linalg.norm(y)) else y, l)

x = np.array([7,1,2])
y = np.array([2,7,1])
lista = [x,y]
print(menorNorma(lista))

'''
===================================================================
7 - Desafio, vamos estimar o valor de pi por meio do Método de 
Monte Carlo. Considere um círculo de raio r=1 centrado na origem 
que está inscrito num quadrado de lado l=2 (veja a figura pi.png).
Vamos estimar o valor de pi comparando a razão da quantidade de 
pontos P_c que "caíram" dentro do círculo (matematicamente P_c
representa o número de pontos em que a distância euclidiana deles
a origem é menor do que r) em relação ao total de pontos P com a
razão da área do círculo em relação ao quadrado, observe:
pi*r^2/l^2 ~= P_c/P
Isto é, utilizando os valores de r^2=1 e l^2=4 estime o valor de pi:
pi/4 ~= P_c/P 
A função que vocês devem implementar deve:
- Receber n como o número de pontos que serão gerados.
- Gerar com numpy n coordenadas x aleatórias.
- Gerar com numpy n coordenas y aleatórias.
- Calcular a quantidade P_c de pontos que caíram dentro do círculo, 
isto é, calcular a distância do ponto I=(x_i,y_i) à origem (0,0) e
contar quantos estão mais próximos da origem do que o raio do círculo
(r=1).
- Retornar o valor de Pi de acordo com a expressão pi = (4*P_c)/P.
Obs: para saber mais sobre o Método de Monte Carlo acesse:
https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Monte_Carlo
===================================================================
'''

def piMonteCarlo(n):
    if isinstance(n, int):
        try:
            array = npr.rand(n,2)
            P_c = 0
            for vetor in array:
                tamanho = np.linalg.norm(vetor)
                if tamanho < 1:
                     P_c += 1
            pi = (4*P_c)/n
            return pi
        except:
            raise ValueError
    else:
        return ("Não é um número inteiro!")
    
print(piMonteCarlo(200000))