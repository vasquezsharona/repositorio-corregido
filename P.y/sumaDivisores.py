def sumaDivisores(num):
    suma=0
    for i  in range(1,num):
        if num%i==0:
            suma+=i
    return suma



def perfectos(num):
    sum=sumaDivisores(num)
    if sum==num:
        return "perfecto"
    else:
        return"no es perfecto"
        
        
        
print(perfectos(28))