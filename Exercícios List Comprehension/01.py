# 1-Crie uma lista com os números pares de 1 a 10.

list = [x for x in range(1,11)
        if x % 2 == 0]
print(list)