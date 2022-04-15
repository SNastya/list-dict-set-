ids = ['1111:271', '1111:190', '1231:106', '1211:104', '1111:201', '1231:120', '1001:205', '1001:223', '1001:127', '1001:236', \
      '1111:229', '1231:286', '1231:195', '1001:279', '1001:124', '1111:292', '1505:219', '1231:259', '1231:253', '1001:220', '1001:202',\
      '1231:103', '1211:249', '1212:275']
count = [111, 3, 13, 111, 9, 5, 17, 10, 13, 3, 16, 4, 16, 11, 18, 12, 14, 4, 3, 2, 14, 14, 10, 10]

items_count = {ids[i]: count[i] for i in range(len(ids))}

#номер 1
a = len({i.split(":")[0] for i in items_count}) #сколько категорий имеется
print(a)

x = [i.split(':')[:-1] for i in ids]
categories = [j for i in x for j in i]
# номер 1
print(len([i for i in categories if categories.count(i) == 1])) #количество категорий встречающихся один раз

# номер2
a = list(zip(categories, count))
dict_category_count = {a[i][0]: 0 for i in range(len(a)) }
for i in range(len(a)):
    dict_category_count[a[i][0]] += a[i][1] 
f = 0 
for i in dict_category_count.values():
    f+= int(i)
print(round(f/len(dict_category_count),1))

# номер3
z = []
for i in range(len(dict_category_count.values())):
    z.append(list(dict_category_count.values())[i] / categories.count(list(dict_category_count.keys())[i]))
print(sum(z)/len(z))

    



# номер 4
def get_key(d, value):
    a = []
    for k, v in d.items():
        if v == value:
            a.append(k)
    return a

max_value = max(count)
print(get_key(items_count, max_value))