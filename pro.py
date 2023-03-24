def common_data(list1, list2):
   result = False
   for x in list1:
      for y in list2:
         if x == y:
            result = True
            return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,3,4,5,6], [9,8,6,5]))

import csv 
Details = ['Name', 'class', 'passoutYear', 'subject']  
rows = [ ['sushma', '2nd', '2023', 'Physics'],  ['john', '3rd', '2022', 'M2'],  ['kushi', '4th', '2021', 'M4']] 
with open('student.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(Details) 
    write.writerows(rows) 

import csv
Deatils = ["Name", "Class","PassoutYear","Subject"]
rows = [['Sushma','2nd','2023','Physics'], ['john', '3rd','2022','M2'], ['Khushi', '4th']]


import csv
list = [['20+30', '50', 'pass'],['10+12', '33', 'fail']]
with open('result.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['marks', 'total', 'result'])
    writer.writerows(list)


import numpy as np 
rows = [ ['Sonu', 'maths', '45'],  
         ['Monu', 'english', '25'],  
         ['Ammu', 'hindi', '35']] 
np.savetxt("student.csv",rows, delimiter =" ",  fmt ='% s')


import csv
Even_list= ['2','4','6','8']
def write_to_csv(Even_list):
     with open('even.csv', 'w', newline='') as csvfile:
         writer = csv.writer(csvfile)
         writer.writerows(Even_list)
write_to_csv(Even_list)  


import csv 
items = [(('fruits', 'apple'), 25), (('vegetables', 'tomato'), 23), (('chocolate', 'kitkat'), 42)]
with open('fruits.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerows(items)

import csv
data = [['name','sonu'],['age','6'],['gender','male']]
with open("student.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)

import csv
from itertools import zip_longest
item1 = ['toys', 'ball', 'cot', 'doll']
item2 = ['fan', 'goat', 'ink', 'jug']
data = [item1, item2]
export_data = zip_longest(*data, fillvalue = '')
with open('items.csv', 'w', encoding="ISO-8859-1", newline='') as file:
      write = csv.writer(file)
      write.writerow(("item1", "item2"))
      write.writerows(export_data)

    
num = [i for i in range(10) if i%2==0 ]
print(num)

num = [i for i in range(10) if i>=5]
print(num)

num = [i for i in range(50) if i%2==0 if i%3==0 if i%3==0]
print(num)

fruits = ["mango" if i%3==0 else "orange" for i in range(10)]
print(fruits)

for i in range(2,4):
        for j in range(1,5):
               print(f"{i}+{j}={i+j}")


list = [[2,4,6,8]]
matrix = [[row[i] for row in list] for i in range(4)]
print(matrix)








