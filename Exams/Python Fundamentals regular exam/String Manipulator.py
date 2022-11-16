text = input()
command = input()
while command != "End":
    split_command = command.split()
    action = split_command[0]

    if action == "Translate":
        char, replacement = split_command[1:]
        text = text.replace(char, replacement)
        print(text)

    elif action == "Includes":
        substring = split_command[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif action == "Start":
        substring = split_command[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")

    elif action == "Lowercase":
        text = text.lower()
        print(text)

    elif action == "FindIndex":
        char = split_command[1]
        index_char = text.rfind(char)
        print(index_char)

    elif action == "Remove":
        start_index = int(split_command[1])
        count = int(split_command[2])
        to_be_removed = text.replace(text[start_index:start_index+count+1], "")
        text = text[0:start_index] + text[start_index+count:]
        print(text)

    command = input()
