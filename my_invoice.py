# Программа "Личный счет"
import json
def invoice():
    with open('invoice.txt', 'r') as f:
        invoice = int(f.read())
    with open('pokupki.json', 'r') as f:
        hist = json.load(f)
    y=True
    while y:
        print('-'*10)
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')
        choice = input('Выберите пункт меню: ')
        print('-'*10)

        if choice == '1':
            print('Текущий счет: ',invoice)
            sum=int(input('Введите сумму (целое положительное число): '))
            invoice+=sum
            with open('invoice.txt', 'w') as f:
                 f.write(str(invoice))
        elif choice == '2':
            sum=int(input('Введите сумму покупки (целое положительное число): '))
            if invoice>=sum:
                pok = input('Введите название покупки: ')
                hist[pok] = sum
                print(hist)
                invoice-=sum
            else:
                print('Недостаточно средств для покупки')
        elif choice == '3':
            if len(hist)!=0:
                print('Список покупок:')
                for i in hist:
                    print('Покупка: ',i,'  Цена: ',hist[i])
            else:
                print('У Вас нет покупок')
        elif choice == '4':
            with open('invoice.txt', 'w') as f:
                f.write(str(invoice))
            with open('pokupki.json', 'w') as f:
                json.dump(hist,f)
            y=False
        else:
            print('Неверный пункт меню')

# print('__name__', __name__)
if __name__ == '__main__':
    invoice()

