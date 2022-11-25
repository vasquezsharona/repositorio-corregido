def primos(num):
    sum=sumaDivisores(num)
    if sum==1:
        return "es primo"
    else:
        return"no es primo"

print(primos())
