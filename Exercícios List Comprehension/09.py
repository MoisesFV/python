# 9-Dada uma lista de números, crie uma nova lista com o dobro de cada número, mas apenas se o número for ímpar

list = [x for x in range(101)]
new_list = [x*2 for x in list
         if x % 2 != 0]
print(new_list)