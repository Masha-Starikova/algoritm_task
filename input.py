def process_input():
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line.split())
    return input_lines

result = process_input()
print(result)