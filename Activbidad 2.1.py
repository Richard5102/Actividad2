import numpy as np
#import builtins
array = np.random.randint(100, size = (5, 4, 3))
#print(array)
minimum = float('inf')
maximum = float('-inf')
inti = 0
intj = 0
intk = 0
minimunloc = [0,0,0]
maximumloc = [0,0,0]
for i in array:
   # print(inti)
    for j in i:
        #print(intj)
        for k in j:
          #print(intk)
          if k < minimum:
            minimum = k
          #  minimunloc.clear()
            minimunloc = [inti, intj, intk] 
          if k > maximum:
            maximum = k
          #  maximumloc.clear()
            maximumloc = [inti, intj, intk]
           
          intk +=1
        intk = 0    
        intj +=1
    intj = 0      
    inti += 1
print(array)      
print("El valor minimo es: ", minimum, "-- Location " + str(minimunloc))         
print("El valor maximo es: ", maximum, "--location " + str(maximumloc))