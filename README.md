#ini adalah numpy 3 dimensi

    import numpy as np

    a = np.array([[[12,32],[23,11],[99,87],
	         [55,66],[56,75],[88,98],			
	         [43,90],[74,33],[86,40]]])

    print(a)
    print("jumlah dimensi {}".format(a.ndim))
    print(a[0][1][1])

#hasil dari print(a[0][1][1]) adalah untuk mengambil angka 11, jika print(a[0][1][0]) maka angka yang di ambil adalah angka 23


#ini adalah numpy 2 dimensi

	import numpy as np
	
	a = np.array([[12,32],
		     [86,40]])
	
	print(a)
	print("jumlah dimensi {}".format(a.ndim))
	print(a[0][1])

#hasil dari print(a[0][1]) adalah untuk mengambil angka 32, jika print(a[1][1]) maka hasil nya adalah angka 40


 #ini adalah numpy 1 dimensi

	import numpy as np
	
	a = np.arange(21)
	
	result = a[3:16:3]
	
	print("Array 1 dimensi:")
	print(a)
	print("Nilai dari index ke-3 sampai ke-15 dengan step kelipatan 3:")
	print(result)

 #hasil dari print(result) adalah print(result) akan mengambil kode result = a[3:16:3] maka hasilnya adalah [3 6 9 12 15], karena nilai dari index ke-3 sampai ke-15 sengan step kelipatan 3, jika result = a[2:10:2] maka hailnya adalah [2 4 6 8], karena nilai dari index ke-2 sampai ke-10 sengan step kelipatan 2

 
