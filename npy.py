import numpy as np

a = np.array([[[12,32],[23,11],[99,87],
	         [55,66],[56,75],[88,98],
	         [43,90],[74,33],[86,40]]])

print(a)
print("jumlah dimensi {}".format(a.ndim))
print(a[0][1][1])