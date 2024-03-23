#ini adalah numpy 3 dimensi

    import numpy as np

    a = np.array([[[12,32],[23,11],[99,87],
	         [55,66],[56,75],[88,98],			
	         [43,90],[74,33],[86,40]]])

    print(a)
    print("jumlah dimensi {}".format(a.ndim))
    print(a[0][1][1])


#ini adalah numpy 2 dimensi

	import numpy as np
	
	a = np.array([[12,32],
		         [86,40]])
	
	print(a)
	print("jumlah dimensi {}".format(a.ndim))
	print(a[0][1])


 #ini adalah numpy 1 dimensi

	import numpy as np
	
	a = np.arange(21)
	
	result = a[3:16:3]
	
	print("Array 1 dimensi:")
	print(a)
	print("Nilai dari index ke-3 sampai ke-15 dengan step kelipatan 3:")
	print(result)
 
