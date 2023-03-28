def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('==' * 10)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('--' * 10)
        return result

    # возвращается функция inner с новым поведением
    return inner




# try:
#     # Тот код который может вызвать исключение
#     age = int(input('Введите кол-во лет: '))
#     print(100 / age)
# except ValueError:
#     # Этот блок срабатывает если было исключение
#     print('Вы ввели не число')
#     print('Введите верное число')
# except ZeroDivisionError:
#     print('Нельзя вводить 0')
# except Exception:
#     print('Неизвестная ошибка!!')
# else:
#     # Выполняется когда нету ошибок
#     print(f'через 4 года тебе будет {age + 4}')
# finally:
#     # Выполняется обязательно есть ошибки или нет
#     print('Выпонить обязательные действия')