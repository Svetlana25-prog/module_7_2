def  custom_write(file_name, strings):
    with open(file_name, 'w+', encoding='utf-8') as f:
        count_line = 1
        strings_positions = {}
        for string in strings:
            b = f.tell()
            strings_positions[(count_line, b)] = string
            f.write(f'{string}\n')
            count_line += 1
        f.close()
        return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)