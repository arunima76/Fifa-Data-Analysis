color_name = ['Black', "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code':c} for f,c in zip(color_name, color_code)])

C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))


C = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))

from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))


color = ['red', 'green', 'orange']
print('-'.join(color))
print(''.join(color))

import itertools
c = itertools.count()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

new_list = [{k:v for k, v in d.items() if k!= 'key1'} for d in original_list]
print("New_list")
print(new_list)



from itertools import chain
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
numbers = list(chain(odd, even))
print(numbers)


from itertools import chain
consonants = ['d', 'f', 'k', 'l', 'n', 'p']
vowels = ['a', 'e', 'i', 'o', 'u']
res = list(chain(consonants, vowels))
res.sort()
print(res)

import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(original_list)
print(new_merged_list)


from itertools import chain
res = list(chain('ABC', 'DEF', 'GHI', 'JKL'))
print(res)


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)





































