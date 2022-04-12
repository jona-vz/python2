from unittest import result


def run():
    '''Challenge: Create a list using list comprehensions with all the numbers
    that are divisible by 4, 6, and 9 at the same time. Just for <100000
    '''

    #it may result by using the 'and' logic operator...
    #result = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    #but it would be more easy if we use the umc = 36 
    result = [i for i in range(1, 100000) if i % 36 == 0]

    print(result)


if __name__ == '__main__':
    run()