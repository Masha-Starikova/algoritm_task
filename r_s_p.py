def solution(A, B):
    point = 0 
    for a, b in zip(A, B):
        if a == 'r':
            if b == 's':
                point += 1
            elif b == 'p':
                point -= 1
        elif a == 's':
            if b == 'p':
                point += 1
            elif b == 'r':
                point -= 1
        else:
            if b == 'r':
                point += 1
            elif b == 's':
                point -= 1
    return point


print(solution(["r","s","p"], ["s","p","r"]))
print(solution(["p","p","p"], ["s","s","s"]))
print(solution(["r","s","p"], ["r","s","p"]))
print(solution(["p","r","s","r","s"], ["s","p","s","p","s"]))

