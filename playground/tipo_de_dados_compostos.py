# s = 'hello world'

# # fatiando (incluindo inicio, excluindo o final)
# ss = s[1:4]  # -> 'ell'
# # print(ss)

# # a partir do início do índice
# ss = s[:4]  # -> 'hell'
# # print(ss)

# # a partir do final do índice
# ss = s[3:]  # -> 'lo world'
# # print(ss)

# # pode usar índice negativo também
# ss = s[2:-2]  # -> 'llo wor'
# # print(ss)

# # saltos
# ss = s[::2]  # -> 'hlowrd'
# # print(ss)
# ss = s[1::2]  # -> 'el ol'
# # print(ss)

# # saltos negativos
# ss = s[::-1]  # -> 'dlrow olleh'
# print(ss)

# print('hello world'.split())

# print('hello, and, welcome'.split(',', maxsplit=1))

# print(' '.join(['hello', 'world']))

# print(','.join(['first line', 'second line']))

## -------------------------------------------

# l = list()
# print(type(l))

# ll = []
# print(type(ll))

## -------------------------------------------

# l = []
# l.append('apple')
# print(l)

# l.append('orange')
# print(l)

## -------------------------------------------

l = ['apple','orange','strawberry','banana']
print(l)

l.insert(3, 'melon')
print(l)

del l[0]
print(l)

print(l.pop())
print(l.pop(0))
print(l)

l[0] = 'apple'
print(l)

l.extend(['pineapple', 'tomato'])
print(l)

l.remove('apple')
print(l)

print(len(l))

for fruit in l:
    print(fruit)
    
## -------------------------------------------


## -------------------------------------------














