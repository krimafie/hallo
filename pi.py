import numpy as np 
import matplotlib.pyplot as plt 

s = 5000
xs = np.random.random_sample(s)*4-2
ys = np.random.random_sample(s)*4-2

c = 0
plt.figure(figsize=(5, 5))
for i in range(0, s):
    x, y = xs[i], ys[i]
    if x**2 + y**2 <=4:
        c+=1
        plt.scatter(x, y, c='blue', alpha=0.2)
    else:
        plt.scatter(x, y, c='red', alpha=0.2)
print(c/s*4)
plt.show()
