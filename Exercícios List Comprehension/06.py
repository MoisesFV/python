# 6-Dada uma lista de números, crie uma nova lista contendo apenas os números pares e maiores que 10.
list = [x for x in range(0,101)]
new_list = [x for x in list
            if x % 2 == 0 and x > 10]
print(new_list)

