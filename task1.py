with open('text.txt', 'r', encoding='UTF-8') as f:
    st, s = [], []
    cook_book = {}
    for i in f.readlines(): #Убираем пустые строчки и записываем списки (рецепты)
        # print(len(i))
        if len(i) != 1:
            s.append(i.rstrip('\n'))
        else:
            st.append(s)
            s = []

    for i in st: #Заполняем словарь значениями
        c = [] #Список словарей
        for j in i[2:]:
            sp = {'ingredient_name': '', 'quantity': '', 'measure': ''}
            line = j.split(' | ')
            sp['ingredient_name'], sp['quantity'], sp['measure'] = line[0], int(line[1]), line[2]
            c.append(sp)
        cook_book[i[0]] = c
    print(cook_book)


