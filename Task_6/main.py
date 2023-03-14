import game

# LOCATIONS
centre = game.Location('Центр')
centre.set_description('Ти в центрі, а вже дуже пізно. Слід рухатись додому...')

sheva = game.Location('Проспект Шевченка')
sheva.set_description('Пройшовши по проспекту Свободи, ти опинився на проспекті Шевченка')

doroshenka = game.Location('Вулиця Дорошенка')
doroshenka.set_description('Ти на велиці Дорошенка. Вдень тут стільки людей і так шумно, а зараз тихо і темно...')

franka = game.Location('Вулиця Франка')
franka.set_description('Ти вийшов на вулиці Франка. Бруківка ледь підсвічується у світлі ліхтаря, що у кінці вулиці...')

kopernyka = game.Location('Вулиця Коперника')
kopernyka.set_description('Ти вийшов на вулиці Коперника. Ти проходиш\
 повз "Дударик" і уявляєш, як тут співають маленькі хлопчики. Аж раптом, чи справді почув спів... ')

str_rynok = game.Location('Стрийський ринок')
str_rynok.set_description('Ти біля Стрийського ринку. Ти згадуєш пані Зеню, яка щовівторка продає зелень з власного городу. Аж раптом...')

sakharova = game.Location('вулиця Сахарова')
sakharova.set_description('')

park = game.Location('Стрийський парк')
park.set_description('')

home = game.Location('Дім')
home.set_description('Ти вдома')

# LINK LOCATIONS
centre.link(sheva, 'наліво')
centre.link(doroshenka, 'направо')
sheva.link(franka, 'направо')
doroshenka.link(kopernyka, 'прямо')
franka.link(str_rynok, 'наліво')
kopernyka.link(sakharova, 'прямо')
str_rynok.link(park, 'прямо')
sakharova.link(park, 'прямо')
park.link(home, 'прямо')

# CHARACTERS

lion = game.Friend('Книжковий лев', 'Мудрий та поважний звір')
lion.set_conversation('Я десь загубив свої окуляри і не можу їх знайти..')
lion.set_feature(1)
sheva.set_character(lion)

zina = game.Friend('Пані Зіна', 'Приємна старша пані')
zina.set_conversation('Я готова тобі щось подарувати, аби допомогти')
zina.set_feature(2)
str_rynok.set_character(zina)

spirit = game.Friend('Дух академіка Сахарова', 'Строгий, проте з місією допомогти')
spirit.set_conversation('Я готовий тобі подарувати дещо. Тобі це пригодиться')
spirit.set_feature(2)
sakharova.set_character(spirit)

grek = game.Enemy('Костя Грек', 'Місцевий божевільний. Краще не попадатись йому на очі і\
 не говорити, бо він не відпустить тебе..Але він уже прямо перед тобою')
grek.set_weakness("невидимка")
franka.set_character(grek)

singer = game.Enemy('Маленький співун', 'Він співає так, що зачаровує, проте це пастка...Допоки він не розпочав, зупини його.')
singer.set_conversation('Я мрію бути як всі хлопці і грати в футбол, але мама віддала мене в "Дударик".')
singer.set_weakness("м'яч")
kopernyka.set_character(singer)

police = game.Enemy('Поліція', 'Що ви робите тут вночі! Жодного шансу на помилку. Відповідайте на питання!')
park.set_character(police)


# ITEMS

glasses = game.Item('окуляри')
glasses.set_description('Тут лежать окуляри')
centre.set_item(glasses)

book = game.Item('книжка')
book.set_description('')
lion.set_item(book)

invisible = game.Item('невидимка')
invisible.set_description('Тут лежить невидимка')
sheva.set_item(invisible)

ball = game.Item("м'яч")
ball.set_description("Тут м'яч")
doroshenka.set_item(ball)

violin = game.Item('скрипка')
violin.set_description('Тут скрипка')
kopernyka.set_item(violin)

# GAME

current_location = centre
backpack = []
lifes = 1

print('\nВітаю у грі "Шлях додому"!\nВаша задача дійти від центру до Колегіуму.\n\
На кожній локації в  рядку ">" можна вводити напрями руху "прямо", "направо", "наліво". Якщо\
 ж у ваш напямок дороги немає, гра про це повідомить.\nТакож з персонажами можна\
 взаємодіяти за домопомгою команд "говорити", "битися", "дати". \nПредмети можна брати за допомогою команди "взяти".')

while lifes > 0:

    print("\n")

    current_location.get_info()

    print('\n')


    inhabitant = current_location.get_character()

    if inhabitant is not None:
        inhabitant.describe()
        print('\n')
        if inhabitant.name == "Поліція":
            print('Скільки коштує проїзд у маршутці у Львові? (тільки цифра)')
            answer1 = input()
            if answer1 != '15':
                lifes -= 1
                print("Неправильно.\nМінус життя. Кількість життів", lifes)
            print('Що таке шпацерувати?')
            answer2 = input()
            if answer2.lower() != 'гуляти':
                lifes -= 1
                print("Неправильно.\nМінус життя. Кількість життів", lifes)
            print('Назва річки у Львові')
            answer3 = input()
            if answer3.lower() != 'полтва':
                lifes -= 1
                print("Неправильно.\nМінус життя. Кількість життів", lifes)
            if lifes > 0:
                print('Тебе відпустили.')
                current_location = current_location.move('прямо')

            else:
                print('Ти програв')

    if current_location == home:
        print("Ти пройшов гру і ти вдома! Вітаємо!")
        break

    item = current_location.get_item()

    if item is not None:
        item.describe()
        print('\n')

    command = input("> ")

    if command in [i[1] for i in current_location.locations]:
        current_location = current_location.move(command)

    elif command == "говорити":

        if inhabitant is not None:
            inhabitant.talk()

    elif command == "дати":
        if inhabitant is not None and inhabitant.clas == 'Friend':
            if inhabitant.item is not None and inhabitant.feature == 1:
                print('Що даси?\n')
                thing = input()
                if thing == 'окуляри':
                    print("Ти взяв " + inhabitant.item.name + " у свій рюкзак\n")
                    backpack.append(inhabitant.item.name )
                    backpack.remove('окуляри')
                    inhabitant.set_item(None)
                    current_location.character = None
                else:
                    print('Це не те, що потрібно було')
            else:
                print("Цей персонаж не має, що тобі дати")
        else:
                print("Цей персонаж не має, що тобі дати")

    elif command == "битися":
        if inhabitant is not None and inhabitant.clas == 'Enemy':
            print("Чим будеш битися?")
            fight_with = input()

            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:

                    print("Ти виграв бій!")
                    current_location.character = None
                else:
                    lifes -= 1
                    if lifes == 0:
                        print('Ти програв.')

            else:
                print("В тебе немає", fight_with)
        else:
            print("Тут немає з ким битись")

    elif command == "взяти":
        if item is not None:
            print("Ти взяв " + item.get_name() + " у свій рюкзак")
            backpack.append(item.get_name())
            current_location.set_item(None)

        elif inhabitant.clas == 'Friend' and inhabitant.feature == 2:
            print("Ти отримав додаткове життя")
            lifes += 1
            current_location.set_character(None)
        else:
            print("Тут немає, що брати")
    else:
        print("Я не знаю як " + command)
