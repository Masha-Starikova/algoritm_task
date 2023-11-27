# Победитель
def olompiada(spisok, N):
    max_count = 0
    for top in range(N - 1):
        count = 1
        for k in range(top+1, N):
            if sorted(spisok[top]) == sorted(spisok[k]):
                count += 1
            if count >= max_count:
                max_count = count
                team = spisok[top]
    return f'Команда: {team} победила {max_count} раз.'




spisok1 = [
["ANTON", "BORIS", "CHRS"],
["BORIS", "ANTON", "CHRIS"],
["MASHA", "ANTON", "VASYA"],
["ANTON", "KATRIN", "SASHA"],
["CHRIS", "BORIS", "ANTON"],
["BORIS", "ANTON", "CHRIS"],
["CHRIS", "ANTON", "BORI"]
]
N1 = len(spisok1)
resultat = olompiada(spisok1, N1)
print(resultat)