def get_data(room_dict, rows, cols):
    import numpy as np
    for i in room_dict:
        array1 = []
        for j in range(1, (rows[i] * cols[i]) + 1):
            array1.append('abcdef')
        array2 = np.array(array1)
        array2.shape = (rows[i], cols[i])
        room_dict[i] = array2
    return room_dict


def result1(cls_name, cls_value, room_dict, rows, cols):
    room_dict = get_data(room_dict, rows, cols)
    x, y, a = 0, 0, 0
    b = 1
    ind = len(cls_name) - 1
    for i in room_dict:
        for j in range(0, cols[i]):
            for k in range(0, rows[i]):
              if ind>=0:
                if j % 2 == 0 and cls_value[a] != 0:
                    x = x + 1
                    room_dict[i][k, j] = cls_name[a] + str(x)
                    cls_value[a] -= 1
              if ind !=0:
                if j % 2 != 0 and cls_value[b] != 0:
                    y = y + 1
                    room_dict[i][k, j] = cls_name[b] + str(y)
                    cls_value[b] -= 1

                if cls_value[a] == 0 and ind >= (a + 2):
                    a += 2
                    x = 0
            if ind !=0:
                if cls_value[b] == 0 and ind >= (b + 2):
                    b += 2
                    y = 0

    return room_dict




