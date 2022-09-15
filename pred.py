import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.chdir('/home/c/cu99893/kamnsv')
import numpy as np
import json
import joblib
import warnings
warnings.filterwarnings("ignore")

def myscaling(vals):
    scale = [(1.472, 3.059),(0.167, 37.617),(0.868, 6.632),(207.753, 510.807),
             (145.993, 356.342),(-2.27, 84.5),(0.111, 100000.0),(0.111, 4060.278)]
    out = []
    for i, x in enumerate(vals):
    	out.append(-1 + 2 * (x-scale[i][0])/(scale[i][1]-scale[i][0]))
    return np.array(out, dtype='<f8')

def scaling(x):
    #return np.array(x, dtype='<f8')
    out = []
    path = '/home/c/cu99893/kamnsv/scaler'
    files = sorted(os.listdir(path))
    for i, f in enumerate(files):
        scaler = joblib.load(path + '/' + f)
        xs = scaler.transform(np.array(x[i], dtype='<f8').reshape(-1, 1)).flatten()
        out.extend(xs)
    return np.array(out, dtype='<f8')

def predict(x):
    x = myscaling(x)
    name = '_'.join(map(str, x))
    if not os.path.isfile(f'data/{name}.npy'):
       np.save('data/'+name, x)
    else:
       x = np.load(f'data/{name}.npy')
    
    process = os.popen(f'./keras2cpp my.model data/{name}.npy')
    line = process.read()
    process.close()          
    y = -1
    try:
        y = np.argmax(json.loads(line))
    except: pass
    return y

        
if __name__=='__main__':
    
    x = input('Enter X:')
    
    y = predict(x.split(' '))
        
    print(y)     