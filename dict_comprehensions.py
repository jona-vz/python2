def run():
    #course solution
    # my_dict = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    #My solution
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)



if __name__ == '__main__':
    run()