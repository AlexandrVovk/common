given_data = [
    {'age': 43, 'name': 'denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'homer'}
]



for _ in  given_data:
    print("type is", type(_['name']), _['name'])
    if _['name'][0].isupper():
#        print(_['name'] + ' is True')
        pass
    else:
#        print(_['name'] + ' is False')
        _['name'] = list(_['name'])
        _['name'][0] = (_['name'][0].upper())
        _['name'] = str(''.join(_['name']))
        print("type is", type(_['name']), _['name'])
#    print(type(_['name']))
#        print(_['name'])
#        print(_)


for i in given_data:
    print(i['name'][0], i['name'][0].isupper())

#        print(type(_['name']))
#        print(type(a))

#        _['name'][0] = a
#        if _['name'][0].isupper():
#            print('now ' + _['name'] + ' is True')
#        else:
#            print('still ' + _['name'] + ' is False')
#print(given_data[0]['name'])


