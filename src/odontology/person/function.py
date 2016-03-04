from person.models import POS_X, POS_Y

def get_position(number):
    number = str(number)
    first = number[0]
    second = number[1]
    if first == '1' or first == '2':
        pos_y = POS_Y[0][1]
    elif first == '4' or first == '3':
        pos_y = POS_Y[1][1]
    elif first == '5' or first == '6':
        pos_y = POS_Y[2][1]
    elif first == '8' or first == '7':
        pos_y = POS_Y[3][1]

    if first == '1' or first == '4' or first == '5' or first == '8':
        pos_x = 175 - (int(second) - 1) * 25
    elif first == '2' or first == '3' or first == '6' or first == '7':
        pos_x = 210 + (int(second) - 1) * 25

    return pos_x, pos_y
