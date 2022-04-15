import re

document_text = 'There are the Food Courts in the cities that seats a lot of people and caters for every taste with dishes from all around the world. \
 The aromatic smells that come from the Food Courts arc so delicious that your mouth will water. \
 In recent years foreign foods have become a regular part of our life.'
document_text_bez_znakov = re.sub(r'[^\w\s]','', document_text) 


list_words = document_text_bez_znakov.split(' ')
set_words = list(set(list_words))
dict_w = {i: 0 for i in list_words}
for i in range(len(dict_w)):
    dict_w[set_words[i]] += list_words.count(set_words[i])
print(dict_w['a'])    
