def init_fields(fields_number, side):
    fields = []
    for k in range(fields_number):
        fields.append([])
        for i in range(side):
            fields[k].append([])
            for j in range(side):
                fields[k][i].append(0)

    return fields

def draw_fields(fields):
    SPASE_FIELDS = 4
    SPASE_CELLSE = 3
    print('   ', end='')
    for k in range(len(fields)):
        for j in range(len(fields[0])):

            _, tmp = coord_atou(0, j)
            print(tmp, end='')
            print(' ' * SPASE_CELLSE, end='')
        print(' ' * (SPASE_FIELDS + 2), end='')
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
    else:
        return '*'

def coord_utoa(vert, horiz):
    j = horiz - 1
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
    }
    i = tmp[vert]
    return (i, j)

def coord_atou(i, j):
    s = 'АБВГДЕЖЗИК'
    vert = s[i]
    horiz = j + 1
    return (vert, horiz)

def add_ship(field: list, ship_len: int, head_coord: tuple, is_horizontal: bool) -> bool:




    return False