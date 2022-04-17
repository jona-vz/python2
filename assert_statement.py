def divisors(num):
    '''Returns a list with all the divisors of the entered number

    Param int num Any positive integer number
    Returns list divisors List of numbers i that num are divisible by them (i)
    '''
    divisors = [i for i in range(1, num+1) if num % i == 0]    
    return divisors

def run():
    num = input("Ingrese un número:   ")
    assert num.isnumeric(), "Debes ingresar un numero positivo"
    print(divisors(int(num)))
    print("Terminó el programa")



if __name__ == '__main__':
    run()

'''
#following the course solution:
def divisors(num):
    #divisors = [i for i in range(1, num+1) if num % i == 0]
    try:
        if num < 0:
            raise ValueError("Debe ser un entero positivo")
        elif num == 0:
            raise ZeroDivisionError("Intenta con otro que no sea cero")    
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False
    except ZeroDivisionError as zde:
        print(zde)
        return False

def run():
    try:
        
        num = int(input("Ingrese un número:   "))
        print(divisors(num))
    except ValueError:
        print("Solo se pueden ingresar numeros enteros")
        
    print("Terminó el programa")



if __name__ == '__main__':
    run()
'''

