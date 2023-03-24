import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)



from itertools import chain
consonants = ['d', 'f', 'k', 'l', 'n', 'p']
vowels = ['a', 'e', 'i', 'o', 'u']
res = list(chain(consonants, vowels))
print(res)


from itertools import chain
res = list(chain('ABC', 'DEF', 'GHI', 'JKL'))
print(res)



from itertools import chain
str1 = "Geeks"
str2 = "for"
st3 = "Geeks"

res = list(chain(str1,str2,st3))
print("before joining:", res)
ans = ''.join(res)
print("After joining:", res)


my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)


my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original list:", my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)

a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []

for x in a:
    if x not in uniq_items:
        uniq_items.append(x)
        dup_items.append(x)

print(dup_items)



from itertools import chain
str1 = "geeks"
str2 = "for"
str3 = "geeks"

res = list(chain(str1, str2, str3))
print("before joining", res)
ans = ''.join(res)
print("After joining", res)


student_list = {'S 001': ['Math', 'Science'], 'S 002':['Math', 'English']}
print(("Original dictionary:"), student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New Dictionary", student_dict)


dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key value count")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key, ' ', value, ' ', count)




from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())


students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print (b,':',students[a][b])



x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items() & set(y.items()):
    print('%s: %s is present in both x and y' %(key, value))


dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
print("Original Dictionary:")
print(dict1)
print("New Dictionary after dropping empty items:")
dict1 = {key:value for (key, value) in dict1.items() if value is not None}
print(dict1)



































