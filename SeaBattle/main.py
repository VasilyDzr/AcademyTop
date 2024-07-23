from impl import *

N = 10

fields = init_fields(2, N)

# fields[0][3][5] = 1

# i, j = coord_utoa('А', 2)
#
# vert, horiz = coord_atou(0, 1)


# print(i, j, vert, horiz)

# Добавим корабль (0 поле, длина кор., коорд начала, направление: False(вертикальный))

is_success = add_ship(fields[0], 2, ('А', 2), False)

if is_success:
    print('Корабль добавлен')

draw_fields(fields)
