# 5-Crie uma lista com as letras maiúsculas de uma string.
string = 'Lorem ipsum dolor sit amet. Et repellendus odit At odio reiciendis aut \
excepturi fuga sed dolorem animi. Et excepturi deleniti qui ratione \
obcaecati rem quam assumenda ab vero ducimus. Qui tenetur autem et galisum \
amet vel quod eligendi.'

capital_letters = [x for x in string
                   if x.isupper()]
print(capital_letters)