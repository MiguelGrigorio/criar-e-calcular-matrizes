import json
import numpy as np

jsonConfig = 'config.json'
txtMatrix = 'matriz.txt'

with open(jsonConfig) as config:
    infos = config.read()

infos = json.loads(infos)

maxValue = infos['maxValue']
minValue = infos['minValue']
qntMatrix = infos['qntMatrix']
order = infos['order']

with open(txtMatrix, 'w') as file:
    for i in range(qntMatrix):
        rand = np.random.randint(low = minValue, high = maxValue, size = (order, order), dtype = int)
        np.savetxt(fname = file, X = rand, fmt = '%g', delimiter = '\t')
        if i != qntMatrix-1:
            file.write('\n')
print('Matrizes criadas.')
