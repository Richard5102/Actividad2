import numpy as np

matriztridimensional = np.array([[[1, 2, 3], [4, 5, 6]],
                            [[7, 8, 9], [10, 11, 12]]])
#3x2x2
print(matriztridimensional)
print("\n*******************************************\n")
print(np.transpose(matriztridimensional, axes=(1,0,2)))
print("\n*******************************************\n")
print(np.transpose(matriztridimensional, axes=(2,1,0)))
print("\n*******************************************\n")
print(np.transpose(matriztridimensional, axes=(2,0,1)))