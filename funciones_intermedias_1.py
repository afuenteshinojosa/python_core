x = [ [5,2,3], [15,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Andrés', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]


def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(key, ":", value)

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'} 
]

iterateDictionary(estudiantes) 

print("-------------")

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])


iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

print("-------------")

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key)
        for item in value:
            print(item)
            
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Andrés', 'Ronaldo', 'Rooney']
}

printInfo(directorio_deportes)