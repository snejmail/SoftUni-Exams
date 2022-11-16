# коригирано по решение от групата във фб:
import re
pattern = r"^(\!)([A-Z][a-z]{2,})(\1):\[([A-Za-z]{8,})\]"
n = int(input())

for _ in range(n):
    string_input = input()

    result = re.finditer(pattern, string_input)
    commands = {}
    numbers = []
    is_valid = False
    for match in result:
        command = match.group(2)
        message = match.group(4)
        for symbol in range(len(message)):
            number = str(ord(message[symbol]))
            numbers.append(number)
        commands[command] = numbers
        is_valid = True

    if is_valid:
        for command in commands:
            print(f"{command}: {' '.join(numbers)}")
    else:
        print("The message is invalid")

# решение, ползващо findall:
# import re
#
# n = int(input())
# pattern = r'(\!)([A-Z][a-z]{2,})(\1):(\[)([A-z]{7,})(\])'
# for _ in range(n):
#     messages = input()
#     matches = re.findall(pattern, messages)
#
#     if len(matches) == 0:
#         print('The message is invalid')
#         continue
#     command = matches[0][1]
#     word = matches[0][4]
#     numbers = ''
#     for char in word:
#         numbers = numbers + str(ord(char)) + ' '
#     print(f'{command}: {numbers}')

# решение, ползващо search:
# import re
#
# pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"
#
# n = int(input())
# for _ in range(n):
#     text = input()
#     match = re.search(pattern, text)
#     if not match:
#         print("The message is invalid")
#     else:
#         command = match.group(1)
#         string = match.group(2)
#         ascii_list = [str(ord(s)) for s in string]
#         print(f"{command}: {' '.join(ascii_list)}")