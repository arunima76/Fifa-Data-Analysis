def common_data(list1, list2):
   result = False
   for x in list1:
      for y in list2:
         if x == y:
            result = True
            return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,3,4,5,6], [9,8.6,5]))

original_list = [10,22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


list1 = [9,7,4,5]
list2 = ['Red', 'Green','Blue']
final_list = list1 + list2 
print(final_list)


s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)


def count_range_in_list(li, min, max):
   ctr = 0
   for x in li:
      if min<= x <= max:
   ctr += 1
   return ctr

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)



