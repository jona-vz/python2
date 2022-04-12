def run():
    '''Challenge: Create a dict using dict comprehensions using the first 1000 
        numbers as keys and the square root as values
    '''

    #it may result by using the sqrt function in  math library
    #but I think it's easier to use i**0.5 <-- and rounded could be great
    result = {i: round(i**0.5, 4) for i in range(1, 1001)}

    print(result)


if __name__ == '__main__':
    run()