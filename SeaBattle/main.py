from impl import *

N = 10 # Размер поля
Gamer = 2

fields = init_fields(Gamer, N)

# Ручная расстановка кораблей (сделано для поля 10Х10 и стандартного набора кораблей)

for gamer in range(Gamer):
    print('Игрок', gamer+1, 'расставляет корабли')
    # Добавление одноклеточных кораблей


    for boat in range(4):
        head_coord_v = input(f'Введите координаты однопалубного №{boat+1}:')
        head_coord = []
        head_coord.append(head_coord_v[0])
        head_coord.append(head_coord_v[1::])
        print(head_coord)
        is_success = add_ship(fields[gamer], 1, head_coord, True)
    # Добавление двух-клеточных кораблей
    for boat_s in range(3):
        head_coord_v = input(f'Введите координаты двухпалубного №{boat_s+1}:')
        head_coord = []
        head_coord.append(head_coord_v[0])
        head_coord.append(head_coord_v[1::])
        is_horizontal = input(f'Горизонтальный (Г) или вертикальный (В):')
        if is_horizontal == 'Г':
            is_horizontal = True
        elif is_horizontal == 'В':
            is_horizontal = False
        is_success = add_ship(fields[gamer], 2, head_coord, is_horizontal)
    # Добавление трех-клеточных кораблей
    for boat_t in range(2):
        head_coord_v = input(f'Введите координаты трехпалубного №{boat_t + 1}:')
        head_coord = []
        head_coord.append(head_coord_v[0])
        head_coord.append(head_coord_v[1::])
        is_horizontal = input(f'Горизонтальный (Г) или вертикальный (В):')
        if is_horizontal == 'Г':
            is_horizontal = True
        elif is_horizontal == 'В':
            is_horizontal = False
        is_success = add_ship(fields[gamer], 3, head_coord, is_horizontal)
    # Добавление четырех-клеточных кораблей
    for boat_f in range(1):
        head_coord_v = input(f'Введите координаты четырехпалубного №{boat_f + 1}:')
        head_coord = []
        head_coord.append(head_coord_v[0])
        head_coord.append(head_coord_v[1::])
        is_horizontal = input(f'Горизонтальный (Г) или вертикальный (В):')
        if is_horizontal == 'Г':
            is_horizontal = True
        elif is_horizontal == 'В':
            is_horizontal = False
        is_success = add_ship(fields[gamer], 4, head_coord, is_horizontal)

# Добавим корабль (0 поле, длина кор., коорд начала, направление: False(вертикальный))

# is_success = add_ship(fields[0], 1, ('А', 2), True)

if is_success:
    print('Корабль добавлен')

draw_fields(fields)


# Атака по корабликам
while True:
    for gamer in range(Gamer):
        print('Игрок', gamer+1, 'атакует')

        attak_coord_v = input(f'Введите координаты атаки:')
        attak_coord = []
        attak_coord.append(attak_coord_v[0])
        attak_coord.append(attak_coord_v[1::])
        if gamer + 1 < Gamer:
            attak_ship(fields[gamer+1], attak_coord)
        else:
            gamer = -1
            attak_ship(fields[gamer + 1], attak_coord)
        draw_fields(fields)

# head_coord = tuple(input(f'Введите координаты однопалубного №{boat+1}:'))

# draw_fields(fields)
