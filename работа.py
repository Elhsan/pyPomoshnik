import os
import webbrowser as wb

def работать():
    print("вы активировали протокол покой!")
    print("\nЕго функции: ")
    print("1)Открыйть телеграм")
    print("2)Открыйть гитхаб")
    print("0)Выйти из протокола покой")

    print('\nпсс.... я разрабатываю это приложение и скоро сдесь будет много функци :> \n')

    x = True
    while x:
        ответ = input("Введите число: ")
        if ответ == "1":
            wb.open('https://github.com/', new=2)
            print("Открываю, сер!")
        if ответ == "2":
            os.startfile(r'C:\Users\user\AppData\Roaming\Telegram Desktop\Telegram.exe')
            print("Понятно, открываю телеграм")
        elif ответ == "выйти":
            x = False
        else:
            print('мой разработчик меня этому не научил :<')
            continue