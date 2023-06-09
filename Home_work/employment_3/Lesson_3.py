from operator import itemgetter
# text = 'а как твои дела эй ты'
# new_text = text.split('а')
# print(new_text)
# text = 'а как а твои а дела а эй а ты'
# new_text_2 = new_text.copy()
# print(new_text_2)
# new_text_3 = 'a'.join(new_text_2)
# print(new_text_3)

#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
def task_1():
    my_list = [1, 1, 4, 5, 1, 3, 6, 6, 8, 3, 5]
    my_list_index = 0
    my_list.sort()
    print(my_list)
    while my_list_index != len(my_list) - 1:
        if my_list[my_list_index] == my_list[my_list_index + 1]:
            my_list.pop(my_list_index)
        elif my_list[my_list_index] != my_list[my_list_index + 1]:
            my_list_index += 1
        else:
            break
    print(my_list)


#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или
# из документации к языку.
def task_2():
    text = 'Большую часть своей службы Каин прошел вместе с Вальхалльскими Ледяными Воинами, переняв у них традиции, ' \
           'сленг, привычки и пристрастие к чаю из танны, хотя так и не смог полюбить холод и мороз, как его любят ' \
           'вальхалльцы.Несмотря на то, что долгая карьера Каина полна героических свершений, все они, по его ' \
           'собственному признанию, совершались им против собственной воли. Он выбрал первым местом своей службы ' \
           'артиллерийский полк специально, чтобы быть подальше от линии фронта. Его первым приоритетом всегда была ' \
           'собственная сохранность и поиск путей для избежания опасности. Несмотря на перманентное нежелание вступать ' \
           'в бой, Каин всегда прекрасно подготовлен для него. В Схоле Прогениум единственным предметом ' \
           '(за исключением спортивных игр), которому он уделял должное внимание была боевая подготовка. ' \
           'Каин описан как исключительный мечник, заслуживший уважение даже от Астартес, сам же он называет свой стиль ' \
           'владения цепным мечом как «инстинктивный». Комиссар также более чем неплохо обращается с лазерным ' \
           'пистолетом, порой поражая цели за пределом прицельной дальности стрельбы. Каин обладает талантом ' \
           'к карточным играм, не стесняясь мухлевания и использования крапленых колод.Каин прекрасно разбирается в ' \
           'людях, в их мотивах, в социальных правилах, нормах и т.д., и эти знания он использует, чтобы укрепить свой ' \
           'образ героя Империума в глазах других. Тонкое понимание психологии и грамотно выстроенное поведение ' \
           'позволяет ему куда реже прибегать к строгим дисциплинарным взысканиям, чем ему полагалось бы в качестве ' \
           'комиссара. Каин всегда активно пытается найти способы избежать казни солдат под его началом даже за самые ' \
           'тяжелые проступки, предпочитая смягчить наказание. Подобные решения в очередной раз позволяют ему ' \
           'поддержать реноме «заботливого комиссара», что в свою очередь побуждает в гвардейцах не ненависть к ' \
           'алому кушаку, а желание сохранить жизнь справедливому командиру. Таким образом, подразделения, в ' \
           'которых служит Каин, всегда обладают высокой моралью и боевой эффективностью. Что, собственно, и ' \
           'требуется от имперского комиссара. Если считать храбростью не отсутствие страха, а умение его преодолевать, ' \
           'то Каина безусловно можно назвать отважным человеком, который вдобавок всегда сохраняет трезвую голову ' \
           'даже в самых тяжелых ситуациях. Кроме того, признавая перед самим собой свои недостатки, он всегда ' \
           'остается слеп к собственным достоинствам, что в какой-то мере можно даже окрестить как «скромность».'
    new_text = text.upper().split(' ')
    counter = 0
    my_dict = {}
    correct_text = []
    count = 0
    while counter != len(new_text):
        new_text.count(new_text[counter])
        my_dict[new_text[counter]] = new_text.count(new_text[counter])
        counter += 1
    sorted_dict = dict(sorted(my_dict.items(), key=itemgetter(1)))
    for key, value in sorted_dict.items():
        correct_text.append(f'Слово "{key}" встречается {value} раз(а)')
    correct_text.reverse()
    #print(correct_text[0:10])
    print('\n10 самых частых слов:')
    while count != 10:
        print(f'    {correct_text[count]}')
        count += 1
#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый
# вариант. *Верните все возможные варианты комплектации рюкзака.
def task_3():
    stuff = {'Нож': 1, 'Топор': 3, 'Котелок': 2, 'Спички': 1, 'Вода': 5, 'Компас': 1, 'Карта': 1, 'Аптечка': 3}
    max_weight = 10
    backpack = 0
    equipment = []
    count = 0
    while backpack < max_weight:
        for key, value in stuff.items():
            if backpack < max_weight:
                equipment.append(list(stuff.keys())[count])
                backpack += stuff.get(key)
                if backpack > max_weight:
                    equipment.pop()
                    count += 1
                count += 1
            else:
                break
    print(f'Вы можете взять с собой в поход:\n{equipment}\nИначе вес рюкзака будет равен {backpack}кг из 10 возможных')


task_1()
task_2()
task_3()