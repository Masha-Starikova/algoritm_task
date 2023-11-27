# перестройка сделать квадратный оффис
def office_area(A, B):
    # A, B в виде [xmin, xmax, ymin, ymax]
    xmin = min(A[0],B[0])
    xmax = max(A[1],B[1])
    ymin = min(A[2], B[2])
    ymax = max(A[3], B[3])
    print('минимальный х,y:', xmin, ymin)
    print('максимальный х,y:', xmax, ymax)

    max_side = max(xmax - xmin, ymax - ymin)
    print('максимальная сторона:', max_side)
    new_offis = max_side**2

    return new_offis



def test_office_area():
    A1 = [1, 4, 2, 6]
    B1 = [3, 7, 1, 5]
    if office_area(A1, B1) == 36:
        print('Ok')
    else:
        print('False')

test_office_area()