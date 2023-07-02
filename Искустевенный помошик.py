import os
import webbrowser as wb
import random as r
import subprocess


рандомная_музыка = [
    'https://www.youtube.com/watch?v=jfKfPfyJRdk',
    'https://www.youtube.com/watch?v=XO2JfS0bwiU',
    'https://www.youtube.com/watch?v=GBrHghh9mgM',
    'https://www.youtube.com/watch?v=B6XlpcEp2q4&pp=ygUl0LvRg9GH0YjQuNC1INC_0LXRgdC90Lgg0LTQu9GPINC40LPRgA%3D%3D'
]
тг = ['телеграм', 'открой телеграм', 'телеграмм', 'тг']
гитхаб = ['гитхаб', 'открой гитхаб', 'open github', 'github']
музыка = ['поставь музыку', 'музыка', 'музочка', 'танцпол']
покой = ['протокол покой', 'отдых', 'покой']
работа = ['протокол работа', 'работа', 'работать']
ии = ['запусти ии', 'ии', 'перцептрон']
новости = ['какие новости', 'последние новости', 'новости']
# разговор = ['поболтаем', 'давай поговорим', 'режжим разговора']
while True:
    вопрос = input("Что вы хотите сделать: ")
    if вопрос.lower() in музыка:
        wb.open(r.choice(рандомная_музыка), new=2)
        print("Загружаю сер!")
    if вопрос in тг:
        os.startfile(r'C:\Users\user\AppData\Roaming\Telegram Desktop\Telegram.exe')
        print("Понятно, открываю телеграм")
    if вопрос in 'ютуб':
        wb.open('https://www.youtube.com/', new=2)
        print("Открываю")
    if вопрос in гитхаб:
        wb.open('https://github.com/', new=2)
        print("Открываю, сер!")
    if вопрос in покой:
        print("Выполняю протокол покой!")
        wb.open('https://www.youtube.com/watch?v=XO2JfS0bwiU', new=2)
        import рабочий_стол 
        
    if вопрос in ии:
        from ii import chat

    if вопрос in 'новости':
        print("Достою информацию!")
        def свежие_ноавости():
            import requests
            from bs4 import BeautifulSoup
            response = requests.get("https://kun.uz")
            soup = BeautifulSoup(response.content, "html.parser")


            paragraphs = soup.find_all("main")
            for paragraph in paragraphs:
                print(paragraph.text)
            return
        свежие_ноавости()

    if вопрос in работа:
        print("Выполняю протокол работа!")
        wb.open('https://www.youtube.com/watch?v=jfKfPfyJRdk', new=2)
        import рабочий_стол 
        os.startfile(r'C:\Users\user\AppData\Local\Programs\Microsoft VS Code\Code.exe')
        from работа import работать 
        работать()

    # if вопрос in разговор:
    #     print("Выполняется протокольный диалог!")                    это багнутый код который я исправлю! 100% потом :>
    #     import разговор

