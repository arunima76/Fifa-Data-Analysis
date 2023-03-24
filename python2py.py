original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


color_name = ['Red', 'Green', 'Black', 'Yellow']
color_code = ['#880076','#770098','#665890','#4560990']
print([{'color_name': f, 'color_code':c,} for f,c in zip(color_name, color_code)])


C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
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


from collections import defaultdict, Counter
str1 = 'w3resource'
my_dict ={}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))


num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)


num_list = [1,2,3,4]
new_dict = current = {}
for name in num_list :
    current[name] = {}
    current = current[name]
print(new_dict)


num = {'n1':[2,3,1], 'n2':[5,1,2], 'n3':[3,2,4]}
sorted_dict = {x:sorted(y) for x,y in num.items()}
print(sorted_dict)





























            