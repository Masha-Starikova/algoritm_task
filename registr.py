word = input('Введите слово: ')
combinations = []

for i in range(len(word)):
    new_combination = word[:i] + word[i].upper() + word[i+1:]
    combinations.append(new_combination)

print(combinations)
