#list_my = [1, 29, 5, 9]
#print(list_my)
#list_my.sort()
#print(list_my[0])

#list_my2 = []
#print(len(list_my2))
#if len(list_my2) == 0:
#    print("lenth is 0")
#else:
#    print("KO")
#    print(list_my2[0])

#given_data = "So the normal way you might go about doing this task in python is using a basic for loop:".split()
#given_data = ['Year', 'has', 12, 'months']
#print(given_data)
#new_data = [str(i) for i in given_data]


#new_data = []
#for i in given_data:
#    i = str(i)
#    new_data.append(i)
#new_data.sort(key=len)
#print(new_data)

data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
                      {'age': 49, 'name': 'Roman', 'sex': 'male'},
                      {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
                      {'age': 47, 'name': 'spike', 'sex': 'female'},
                      {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
                      {'age': 49, 'name': 'Batman', 'sex': 'male'},
                      {'age': 37, 'name': 'claus', 'sex': 'male'},
                      {'age': 55, 'name': 'Frank', 'sex': 'female'},
                      {'age': 83, 'name': 'homer', 'sex': 'male'}
]

key = 'age'

data_new = [i[key] for i in data]

data_new.sort()
print(data_new[0])
print(data[4])

data_new2 = sorted(data, key=lambda k: k[key])
print(data_new2[0])


#for i in  given_data:
#    print(i)
#    i.pop("age")
#    print(i)

#value = 'SuperMan'
#print(value)
#for data_list in data:
#    if value in data_list:
#        print(data_list)
#    print(data_list.items())
#    if 'SuperMan' in data_list:
#        print("ok", list(data_list))


#d = [{'age': 31, 'name': 'SuperMan'}]
#a = 'SuperMan'
#new_list = []
#for i in data:
#    if a in i.values():
#        print("ok", list(i))
#        new_list.append(i)
#    else:
#        print("KO")
#print(new_list)

    #print(given_data)


#for i in given_data:
#    print(i['name'][0], i['name'][0].isupper())

#        print(type(_['name']))
#        print(type(a))

#        _['name'][0] = a
#        if _['name'][0].isupper():
#            print('now ' + _['name'] + ' is True')
#        else:
#            print('still ' + _['name'] + ' is False')
#print(given_data[0]['name'])


