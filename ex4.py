def val_cheker(verify):

    def cube(function):

        def cube1(number):
            print(f'Возводим куб в число {number}')
            if not verify(number):
                raise ValueError
            return function(number)
        return cube1
    return cube

@val_cheker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

value = int(input('Введите число: '))
result = calc_cube(value)
print(f'Ответ: {result}')
