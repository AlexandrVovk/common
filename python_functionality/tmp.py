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
#    print(_['name'])
    if _['name'][0].isupper():
        print(_['name'] + ' is True')
    else:
        print(_['name'] + ' is False \nwe will change')
        _['name'] = list(_['name'])
        _['name'][0] = (_['name'][0].upper())
        _['name'][0] = str(''.join(_['name']))
        print(type(_['name']))
#        print(type(a))

#        _['name'][0] = a
#        if _['name'][0].isupper():
#            print('now ' + _['name'] + ' is True')
#        else:
#            print('still ' + _['name'] + ' is False')


#print(given_data[0]['name'])