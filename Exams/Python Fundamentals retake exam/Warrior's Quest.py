skill = input()
command = input()

while command != "For Azeroth":
    split_command = command.split()
    action = split_command[0]

    if action == "GladiatorStance":
        skill = skill.upper()
        print(skill)
    elif action == "DefensiveStance":
        skill = skill.lower()
        print(skill)
    elif action == "Dispel":
        index, letter = int(split_command[1]), split_command[2]
        if 0 <= index < len(skill):
            skill = skill.replace(skill[index], letter, 1)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif split_command[0:2] == ['Target', 'Change']:
        first_substring, second_substring = split_command[2:]
        if first_substring in skill:
            skill = skill.replace(first_substring, second_substring)
        print(skill)
    elif split_command[0:2] == ['Target', 'Remove']:
        substring = split_command[2]
        if substring in skill:
            skill = skill.replace(substring, "")
            print(skill)
    elif command == "For Azeroth":
        break
    else:
        print("Command doesn't exist!")

    command = input()
