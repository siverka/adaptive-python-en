import numpy as np
from urllib.request import urlopen
filename = 'https://stepic.org/media/attachments/lesson/16462/boston_houses.csv'
f = urlopen(filename)
data = np.loadtxt(f, delimiter=',', skiprows=1)
print(data.mean(axis=0))
