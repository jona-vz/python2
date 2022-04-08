def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"name": "Jonathan", "lastname": "Vasquez"}

    super_list = [
        {"name": "Jonathan", "lastname": "Vasquez"},
        {"name": "Facundo", "lastname": "Garcia"},
        {"name": "Miguel", "lastname": "Torres"},
        {"name": "Pepe", "lastname": "Rodelo"},
        {"name": "Susana", "lastname": "Martinez"},
        {"name": "Jose", "lastname": "Hernandez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for person in super_list:
        print(person["name"], "-", person["lastname"])

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()