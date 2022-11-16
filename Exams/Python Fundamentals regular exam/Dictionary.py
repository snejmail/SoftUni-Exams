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
