matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matriz[1][1])


#for i in matriz:
 #   print(i)
for i in range (len(matriz)):
    for j in range (len( matriz)):
     #   for k in range (len(matriz)):
           print (matriz [i][j],end=" ")
