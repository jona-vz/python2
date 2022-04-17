def read():
    '''Just read numbers.txt file and return a list with all the content numbers
    '''
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)


def write():
    '''Writes the list of names <names> on names.txt
    '''
    names = ["Jona", "Facundo", "Miguel", "Pepe", "Diana", "Rocío", "Ñaldo"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def append():
    '''Append the list of names <names> on names.txt
    '''
    names = ["Jonathan", "Facundo", "Miguel", "Pepe", "Diana", "Rocío", "Ñaldo"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()
    append()


if __name__ == '__main__':
    run()