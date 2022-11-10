import random
import numpy as np
list = []
for num in range(1,1000):
    list.append(random.randrange(10,99))
numbers = np.array(list)
print (numbers)