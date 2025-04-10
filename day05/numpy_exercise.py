import numpy as np

a = np.arange(12)
b = a.reshape(3, 4)


print(a,'\n',b)

print(b[1,2])

print(np.mean(b, axis=0))

print(b[b>5])

add_row=np.array([[1],[2],[3]])

print(b+add_row)