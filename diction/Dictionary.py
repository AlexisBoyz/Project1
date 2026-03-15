# country = []  -   это называется СПИСОК
# country = {}  -   это называется СЛОВАРЬ (Тут могут быть разные типы данных (int, float, str ,bool), однако, нельзя использовать списки
# country = ()  -   это называется КОРТЕЖ

person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Wick',
        'age' : 43,
        'profession' : 'Killer',
        'address' : ['Country: USA','City: New York', 'Street: West Broadway 45', 'apartment: 28'],
        'grades': {
            'math' : 5,
            'physics' : 4
        }
    },
    'user_2': {
        'first_name': 'Сергей',
        'last_name': 'Бурунов',
        'age' : 56,
        'profession': 'actor',
        'address': ['Country: Russia', 'City: Moscow','Street: Измайловская 666', 'apartment: 66']
    }
}

print(person['user_1']['grades']['math'])