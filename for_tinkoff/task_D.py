def drive_elevators(n, list_elevators):
#    print("полученный список:", list_elevators)
    result_list = [list_elevators[0]]
    time_list = [list_elevators[0]]
    for i in range(1, n):
        # Нижний этаж.
        s = list_elevators[i]
        # Вверхний этаж.
        f = list_elevators[i-1]
        if s[0] == f[1]:
            time_list.append(s)
            if len((time_list)>len(result_list)):
                result_list = time_list.copy()
        else:
            time_list = [list_elevators[0]]         
    return len(result_list)


def data_input():
    list_elevators = []
    n = int(input())
    for _ in range(n):
        elevator = list(map(int, input().split()))
        list_elevators.append(elevator)
        list_elevators.sort(key=lambda x: (x[0], x[1]))
    return n, list_elevators

n, a = data_input()
print(drive_elevators(n, a))

