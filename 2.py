shedule = {
    '1001': ['пн', 'вс'],
    '1231': ['пн', 'вт'],
    '1232': ['ср', 'чт', 'пт'],
    '1280': ['ср', 'пт', 'вс'],
    '1282': ['чт'],
    '1290': ['пт', 'вс'],
    '1303': ['вт', 'вс'],
}

unique_days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
set_unique_days = set(unique_days)

days = {j for i in shedule.values() for j in i }
print("Дни, когда никто не может дежурить: ", set_unique_days-days)

dict_workers = {i: 0 for i in unique_days}
list_of_days = [ j for i in shedule.values() for j in i]

for i in unique_days:
    dict_workers[i] = list_of_days.count(i)
    
print("Количество сотрудников по дням недели:", dict_workers)
