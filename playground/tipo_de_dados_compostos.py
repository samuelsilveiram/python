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

# l = ['apple','orange','strawberry','banana']
# print(l)

# l.insert(3, 'melon')
# print(l)

# del l[0]
# print(l)

# print(l.pop())
# print(l.pop(0))
# print(l)

# l[0] = 'apple'
# print(l)

# l.extend(['pineapple', 'tomato'])
# print(l)

# l.remove('apple')
# print(l)

# print(len(l))

# for fruit in l:
#     print(fruit)
    
## -------------------------------------------

# l = ['apple','orange','strawberry','banana', 'watermelon', 'mixirica']
# print(l)

# print(l[0])

# print(l[3])

# print(l[-1])

# print(l[2:4])

# print([10,20,30,40][::-1])

## -------------------------------------------

# l = ['apple','orange','strawberry','banana', 'watermelon', 'mixirica']
# print(l)

# print('apple' in l)

# print('basketball' in l)

## -------------------------------------------

# l = [25, 3, 14] + [5, 4] + [101, 2]
# print(l)

# l = ['apple','orange'] * 3
# print(l)

## -------------------------------------------

# l = ['apple','orange','strawberry','banana', 'watermelon', 'mixirica']
# l.reverse()
# print(l)
# l.reverse()
# print(l)

## -------------------------------------------

# fruit = ["orange", "apple", "strawberry", "banana", "apricot"]
# print(fruit)
# fruit.sort()
# print(fruit)
# fruit.sort(reverse=True)
# print(fruit)

## -------------------------------------------

l = [10,5,25,100,250,1,8]
print("L: {}".format(l))

l2 = l
print("L2: {}".format(l2))
l.append("BOOM!")

l3 = l[:]
print("L3: {}".format(l3))
l3.append(9876)

print("L: {}".format(l))
print("L2: {}".format(l2))
print("L3: {}".format(l3))

## -------------------------------------------


## -------------------------------------------












