import numpy as np

txtMatrix = 'matriz.txt'
txtRel = 'relatorio.txt'

with open(txtMatrix, 'r') as file:
    matTxt = file.readlines()
    allMatrix = np.genfromtxt(fname = file.name, dtype=int)
qntMatrix = matTxt.count('\n')+1
matList = np.split(allMatrix, qntMatrix)

with open(txtRel, 'w+') as rel:
    j = 1
    for i in matList:
        if j != 1:
            rel.write('\n')

        rel.write(f'Matriz {j}:\n')
        rel.write(f'{i}\n\n')
        try:
            inv = np.linalg.inv(i)
            rel.write(f'Matriz {j} inversa:\n {inv}\n\n')
            detinv = np.linalg.det(inv)
            detinv = f'Determinante da inversa da matriz {j}: {detinv}'
            rel.write(f'{detinv}')
            l = len(detinv)
            rel.write('\n{}\n'.format('='*l))
        except:
            inv = f'Matriz {j} inversa: Não há matriz inversa'
            rel.write(inv)
            l = len(inv)
            rel.write('\n{}\n'.format('='*l))
        j+=1
    rel.write('\nAutor: Miguel Grigorio')

print('Relatório criado.')