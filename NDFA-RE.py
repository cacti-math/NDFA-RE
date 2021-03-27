M={}
M['Q']=[]
for x in range(3):
    M['Q'].append('q'+str(x+1))

M['sigma']={'0','1'}
M['delta']={'q1':{'0':'q2','1':'q3'},
            'q2':{'0':'q1','1':'q3 '},
            'q3':{'0':'q2','1':'q2'}}

M['q1']='q1'

M['F']=['q2','q3']

r=M['F']
n=len(M['Q'])

def R0(i,j):
    A=set()
    u=M['Q'][i-1]
    w=M['Q'][j-1]    
    if i==j:
        A={'e'}
    for a in M['delta'][u].keys():
            if w in M['delta'][u][a]:
               A=A|{a}
            cad=str()
            for r in A:
                cad += str('+')+str(r)
    return cad

def R(i,j,k):
    A=str()
    if k==0:
        A=R0(i,j)
    else:
        A=str('(')+R(i,k,k-1)+str(')(')+R(k,k,k-1)+str(')')+str('*')+str('+')+str('(')+R(i,j,k-1)+str(')')
    return A

H=[]
for x in M['F']:
    H.append(M['Q'].index(x))


S=str()
for m in H:
    S+=R(1,m,n)

print(R0(2,1))
print(S)
