import pickle
import numpy as np
import matplotlib.pyplot as plt
import time
%matplotlib inline 

# Ouvrir des données stockées dans un fichier .pk
data = pickle.load(open('data.pk','rb'), encoding='latin1')
print("Available keys:" , data.keys())

plt.imshow(data['original'], cmap='gray');
plt.figure()
plt.imshow(data['observations'], cmap='gray');