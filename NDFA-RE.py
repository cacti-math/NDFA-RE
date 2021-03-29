####Este programa transoforma un Autómata finito no determinístico a una expresión regular####
# Utilizaremos las funciones definidas en el programa creado por Angel
from NFAtoDFA import NFAtoDFA

#Dado K un Autómata finito no determinístico lo convertimos en uno determinístico
K={}

#Definimos los estados del autómata
K['Q']=['q0','q1']

#Definimos el alfabeto del autómata
K['Sigma']=['0','1']

#Definimos la función de transición del autómata
K['delta']={'q0':{'0':['q0'],'1':['q0','q1']},
             'q1':{'0':[],'1':[]}}

#Definimos el estado inicial del autómata
K['q0']='q0'

#Definimos el conjunto de estados finales del autómata
K['F']=['q1']

#Sea T el autómata finito deterministico generado a partir de K
T = NFAtoDFA(K)
#print(K)



#definimos la función suma que nos dara la sauma de dos elementos en el formato buscado
def suma(a, b):
    return '[+, '+ str(a) + ' ,' + str(b) + ']'

#print(suma(3,5))

#definimos la función cKleene que nos dara la cerra de Kleene en el formato buscado
def cKleene(a):
    return '[*, ' + str(a) + ']'

#print (cKleene(4))

#definimos la función concaetacion que nos dara la concatenacion de dos elementos
def producto(a,b):
    return '[x, '+ str(a) + ' ,' + str(b) + ']'

#print (concatenacion(4,5))


#definimos la r(G,i,j,k) de forma recursiva como en el texto a partir de R(i,j,k) considerando un AFD G
def r(G,i,j,k):
    R_ij = set()
    #Primero el caso cuando k = 0
    if k == 0:
        if i == j:
            R_ij = R_ij | {'e'}
        for a in G['Sigma']:
        #Esto es una idea, pq no funciona por alguna razón
            if G['delta'][G['Q'][i]][a] == G['Q'][j]:
                R_ij = R_ij | T['Q'][j]

        #Convertirmos al conjunto R_ij en una lista
        R_ij.sort()
        r_ij = R_ij[0]
        for l in range(len(R_ij)-1):
            r_ij = suma(r_ij, R_ij[l+1])
        return r_ij
    #Utilizando recursión definimos la expresión regular
    return suma(producto(producto(r(G,i, j, k - 1), cKleene(r(G,k, k, k - 1))), r(G,k, j, k - 1)), r(G,i, j, k - 1))


#Finalmente la función que tomará el AFD y lo transformará en expresión regular
def NDFAtoRE(A):
    B = NFAtoDFA(A)
    n = len(B['Q'])
    F = []

    #Esto no funciona, pero lo que intenta es ver que indíces tienen los estados finales de B (B['F']) respecto de la lista T['Q']
    #para usar esos índices j en en r(1, j, n)
    for u in B['F']:
        for v in range(len(B['Q'])):
            #Esto es lo que no funciona, buscar manera alternativa de hacerlo
            if u == B['Q'][v]:
                F.append(v)
    rf = r(B,1,F[0],n)
    for j in range(len(F) - 1):
        rf = suma(rf, r(B,1,F[j+1],n))
    return rf

#print(NDFAtoRE(K))