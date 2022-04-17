DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #working with comprehensions and high order functions
    #Objective:
    #1-show all the python devs using comprehensions
    all_python_devs = [worker['name'] for worker in DATA if worker['language']== 'python']
    #2-show all the Platzi workers using comprehensions
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization']== 'Platzi']
    #3-show all adults of data using filter and lambda
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    #4-Using map and lambda add the old atribute to your data with true if person
    #  are older than that and false in other case
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    print('All python devs')
    for worker in all_python_devs:
        print(worker)

    print()
    print('All platzi workers')
    for worker in all_platzi_workers:
        print(worker)

    print()
    print('Adults')
    for worker in adults:
        print(worker)
    
    print()
    print('Old people')
    for worker in old_people:
        print(worker)
    

if __name__ == '__main__':
    run()