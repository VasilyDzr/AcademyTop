def init_fields(fields_number, side):
    """
    Создание основы полей морского боя
    :param fields_number: количество полей
    :param side: размеры стороны поля (квадратного)
    :return: подготовленное поле для заполнения
    """
    fields = []
    for k in range(fields_number):
        fields.append([])
        for i in range(side):
            fields[k].append([])
            for j in range(side):
                fields[k][i].append(0)

    return fields

def draw_fields(fields):
    """
    Заполенение поля символами
    :param fields:
    :return:
    """
    SPASE_FIELDS = 4
    SPASE_CELLSE = 3
    print('   ', end='')
    for k in range(len(fields)):
        for j in range(len(fields[0])):

            _, tmp = coord_atou(0, j)
            if tmp < 10:
                print(tmp, end='')
                print(' ' * SPASE_CELLSE, end='')
            else:
                print(tmp, end='')
                print(' ' * (SPASE_CELLSE-1), end='')
        print(' ' * (SPASE_FIELDS + 3), end='')
    print()

    for i in range(len(fields[0])):
        for k in range(len(fields)):
            for j in range(len(fields[0])):
                if j == 0:
                    perem = coord_atou(i, j)
                    print(perem[0], ' ', end='')
                print(get_cell_simbul(fields[k][i][j]), ' ' * SPASE_CELLSE, end='', sep='')
            if k < len(fields) - 1:
                print(' ' * SPASE_FIELDS, end='')
        print('')

def get_cell_simbul(value):
    """
    Замена символов в ячейке на заданный для данного типа корабля
    :param value:
    :return:
    """
    if value == 0:
        return '.'
    elif value == 1:
        return '1'
    elif value == 2:
        return '2'
    elif value == 3:
        return '3'
    elif value == 4:
        return '4'
    elif value == -1:
        return 'X'
    elif value == 'Y':
        return 'Y'
    elif value == 'N':
        return 'N'
    else:
        return '*'

def coord_utoa(vert, horiz):
    """
    Перевод координат пользовательских на програмные (A 2 >> 0 1)
    :param vert: координаты вертикальные
    :param horiz: координаты горизонтальные
    :return:
    """
    j = int(horiz) - 1
    tmp = {
        'А': 0,
        'Б': 1,
        'В': 2,
        'Г': 3,
        'Д': 4,
        'Е': 5,
        'Ж': 6,
        'З': 7,
        'И': 8,
        'К': 9,
        'Л': 10,
        'М': 11,
        'Н': 12,
        'О': 13,
        'П': 14,
        'Р': 15,
        'С': 16,
        'Т': 17,
    }
    i = tmp[vert]
    return (i, j)

def coord_atou(i, j):
    """
    Перевод координат програмных на пользовательские (0 1 >> A 2)
    :param i: координаты вертикальные
    :param j: координаты горизонтальные
    :return:
    """
    s = 'АБВГДЕЖЗИКЛМНОПРСТ'
    vert = s[i]
    horiz = j + 1
    return (vert, horiz)

def add_ship(fields: list, ship_len: int, head_coord: list, is_horizontal: bool) -> bool:
    """
    Добаление корабля на поле, если корабль не выходит за границы поля
    :param field: номер поля
    :param ship_len: длина корабля
    :param head_coord: начальная точка в програмных координатах
    :param is_horizontal: вертикальный / горизонтальный корабль
    :return: Получилось добавить / не получилось
    """
    vert, horiz = coord_utoa(head_coord[0], head_coord[1])
    if horiz + ship_len > len((fields[0])) or vert + ship_len > len((fields[0])):
        print('Корабль выходит за игровое поле')
        return False
    else:
        # Меняет символ корабля на нужный
        for i in range(ship_len):
            fields[vert][horiz] = ship_len
            get_cell_simbul(ship_len)
            if is_horizontal:
                horiz += 1
            else:
                vert += 1
        # Окружает корабль полем Х (понятно, что сделанно криво, но не понятно, как сделать по нормальному)
        # vert, horiz = coord_utoa(head_coord[0], head_coord[1])
        # if is_horizontal:
        #
        #     # Когда корабль не прижат к стенкам
        #     if vert != 0 and vert != len((fields[0])) and horiz != 0 and horiz != len((fields[0]))-1:
        #         for i in range(ship_len):
        #             fields[vert - 1][horiz] = -1
        #             fields[vert + 1][horiz] = -1
        #             horiz += 1
        #         for i in range(3):
        #             fields[vert - 1][horiz-ship_len-1] = -1
        #             fields[vert - 1][horiz] = -1
        #             vert += 1
        #
        #     # Когда корабль прижат к верхнему краю поля, но не в углу
        #     elif vert == 0 and horiz != 0 and horiz != len((fields[0])) and horiz != 0:
        #         for i in range(ship_len):
        #             fields[vert + 1][horiz - ship_len] = -1
        #             horiz += 1
        #         for i in range(2):
        #             fields[vert][horiz - ship_len] = -1
        #             fields[vert][horiz - ship_len * 2 - 1] = -1
        #             vert += 1
        #
        #     # Когда корабль прижат к нижнему краю поля, но не в углу
        #     elif vert == len((fields[0]))-1 and horiz != 0 and horiz != len((fields[0]))-1:
        #         for i in range(ship_len):
        #             fields[vert - 1][horiz - ship_len] = -1
        #
        #             horiz += 1
        #         for i in range(2):
        #             fields[vert - 1][horiz - ship_len] = -1
        #             fields[vert - 1][horiz - ship_len * 2 - 1] = -1
        #             vert += 1
        #
        #     # Когда корабль прижат к правой стенки
        #     elif vert != 0 and vert != len((fields[0])) and horiz == len((fields[0]))-1:
        #         for i in range(ship_len):
        #             fields[vert - 1][len((fields[0]))-1] = -1
        #             fields[vert + 1][len((fields[0]))-1] = -1
        #             horiz += 1
        #         for i in range(3):
        #             fields[vert - 1][len((fields[0]))-2] = -1
        #             vert += 1
        #
        #     # Когда корабль прижат к левой стенки
        #     elif vert != 0 and vert != len((fields[0])) and horiz == 0:
        #         for i in range(ship_len):
        #             fields[vert - 1][horiz] = -1
        #             fields[vert + 1][horiz] = -1
        #             horiz += 1
        #         for i in range(3):
        #             fields[vert - 1][horiz] = -1
        #             vert += 1
        #
        #     # Когда корабль прижат к верхн. прав. углу
        #     elif vert == 0 and horiz == 0:
        #         for i in range(ship_len):
        #             fields[vert + 1][horiz] = -1
        #             horiz += 1
        #         for i in range(2):
        #             fields[vert ][horiz] = -1
        #             vert += 1



    return True

def attak_ship(field, attak_coord):
    vert, horiz = coord_utoa(attak_coord[0], attak_coord[1])
    if field[vert][horiz] == 1 or field[vert][horiz] == 2 or field[vert][horiz] == 3 or field[vert][horiz] == 4:
        field[vert][horiz] = 'Y'
        get_cell_simbul(field[vert][horiz])
        print('Вы попали')
    else:
        field[vert][horiz] = 'N'
        get_cell_simbul(field[vert][horiz])
        print('Вы не попали')
