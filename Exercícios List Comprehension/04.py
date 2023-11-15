# 4-Dada uma lista de números, crie uma nova lista apenas com os números maiores que 5.
list = [x for x in range(1,101)]
new_list = [x for x in list
            if x > 5]
print(new_list)