import numpy as np

#perkalian matriks

bil1 = np.array([10,11,12,13,14])
bil2 = np.array([20,21,22,23,24])

for i in range(0,len(bil1)):
    operate = bil1[i]*bil2[i]
    print(operate)
