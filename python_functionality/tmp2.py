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

data = ['homer', 'Alex', 'Olga']
data1 = 'homer'
#print(type(data1))
print(given_data)
data1 = list(given_data)
print(type(given_data))
#data1[0] = given_data[0].upper()
#print(len(given_data))
for _ in range(len(given_data)):
    print(_); print(data1[_]['name'])

#for _ in  data1:
#    print(data1[0]['name'])
#data1 = str("".join(data1))
#print(type(data1))
#print(data1)
#data[0] =

#for i in data:
#    print(i)
#    i = i.upper()
#    print(i)

