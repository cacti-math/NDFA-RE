'''Ejemplo Automata finito determinista - EJERCICIO DE LAS NOTAS 2.1'''

'''Construimos Diccionario vacío y despues lo llenamos con los 5 elementos de un automata'''
M1={}

'''Estados del automata'''
M1['Q']=['q0','q1','q2','q3']

'''Alfabeto'''
M1['Sigma']=['0','1']

'''Función de transición'''
M1['delta']={'q0':{'0':'q2','1':'q1'},
             'q1':{'0':'q3','1':'q0'},
             'q2':{'0':'q0','1':'q3'},
             'q3':{'0':'q1','1':'q2'}}

'''Estado inicial'''
M1['q0']='q0'

'''Conjunto de estados finales'''
M1['F']=['q0']

#d=M1['delta']
#print(d['q2']['1'])

#print(M1)

'''Funcion que recibe un AFD (DFA) y una cadena y nos indica si la reconoce o no'''
def aceptacadenaDFA(A,w):
    delta=A['delta']
    q=A['q0']
    if len(w)!=0:
        for i in range(len(w)):
            q=delta[q][w[i]]
    return(q in A['F'])

'''El ejemplo de 2.1 q estamos trabajando'''
#print(aceptacadenaDFA(M1,'010111'))

'''Ejemplo de automata finito no determinista - Figura 2.2 de las notas'''
M2={}

'''Estados del automata'''
M2['Q']=[]
for x in range(5): M2['Q'].append('q'+str(x))

'''Alfabeto'''
M2['Sigma']=['0','1']

'''Funcion delta'''
M2['delta']={'q0':{'0':['q0','q3'],'1':['q0','q1']},
             'q1':{'0':[],'1':['q2']},
             'q2':{'0':['q2'],'1':['q2']},
             'q3':{'0':['q4'],'1':[]},
             'q4':{'0':['q4'],'1':['q4']}}

M2['q0']='q0'

M2['F']=['q2','q4']
 
#print(M2)

'''Funcion que recibe un NFA y una cadena y nos indica si la reconoce o no'''
def aceptacadenaNFA(A,w):
    delta = A['delta']
    X = {A['q0']}
    for i in range(len(w)):
        if X==set():
            break
        Y=set()
        for r in X:
            Y=Y|set(delta[r][w[i]])
        X=Y
    return(not X & set(A['F']) == set())

#print(aceptacadenaNFA(M2,'010100101'))

'''Transformacion de un NFA a un DFA'''

'''Esta funcion recibe una lista de listas y un elemento cualquiera. Agrega a cada 
lista ese elemento y devuelve la nueva lista de listas'''
def union(Q,q):
    for i in range(len(Q)):
        Q[i].append(q)
    return(Q)

'''Recibe una lista y devuelve el conjunto potencia representado por listas
(El procedimiento se hace con recursion)'''
'''definicion recursiva del conjunto potencia, complejidad 2^n'''
def conjuntoPotencia(Q):
    if len(Q)==0:
        return [[]]
    return conjuntoPotencia(Q[1:])+union(conjuntoPotencia(Q[1:]),Q[0])

'''Recibe el conjunto potencia y a cada elemento lo ordena y lo transforma
en una cadena para poderlo usar como llaves en los nuevos diccionarios que
se crearan'''
def transformar_a_cadena(P):
    Q=[]
    for r in P:
        r.sort()
        Q.append(str(r))
    return Q

'''Recibe la funcion delta del NFA y devuelve la correspondiente en su DFA'''
def delta_nueva(P,A):
    Sigma=A['Sigma']
    delta=A['delta']
    deltan={}
    for x in P:
        x.sort()
        y={}
        for a in Sigma:
            H=set()
            for r in x:
               H = H | set(delta[r][a])
            H=list(H)
            H.sort()
            y[a]=str(H)
        deltan[str(x)]=y
    return(deltan)

'''Esta funcion retorna el conjunto de aceptacion del DFA'''
def Conjunto_aceptacion(P,A):
    F=set(A['F'])
    X=[]
    for x in P:
        if F & set(x)!=set():
            x.sort()
            X.append(str(x))
    return X

'''Recibe un NFA y devuelve su respectivo DFA'''
def NFAtoDFA(A):
    M = {}
    S=conjuntoPotencia(A['Q'])
    M['Q'] = transformar_a_cadena(S)
    M['Sigma'] = A['Sigma']
    M['delta'] = delta_nueva(S,A)
    M['q0'] = str([A['q0']])
    M['F'] =Conjunto_aceptacion(S,A)
    return(M)

M=NFAtoDFA(M2)

'''Acá hay algunas ejemplos'''
#print(aceptacadenaDFA(M,'101010101101010'))

#######EJEPLO################

M3={}

M3['Q']=['q0','q1']

M3['Sigma']=['0','1']

M3['delta']={'q0':{'0':['q0'],'1':['q0','q1']},
             'q1':{'0':[],'1':[]}}

M3['q0']='q0'

M3['F']=['q1']

M4=NFAtoDFA(M3)

#print(M4)

'''Si tienen alguna duda u observacion, me pueden escribir a 
angel.elias21@gmail.com o me escriben por telegram'''