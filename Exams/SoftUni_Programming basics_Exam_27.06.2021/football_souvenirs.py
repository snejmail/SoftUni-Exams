football_team = input()
souvenir_type = input()
souvenirs_count = int(input())
souvenir_price = 0.0
invalid = False

if football_team == "Argentina":
    if souvenir_type == "flags":
        souvenir_price = 3.25
    elif souvenir_type == "caps":
        souvenir_price = 7.20
    elif souvenir_type == "posters":
        souvenir_price = 5.10
    elif souvenir_type == "stickers":
        souvenir_price = 1.25
    else:
        print("Invalid stock!")
        invalid = True

elif football_team == "Brazil":
    if souvenir_type == "flags":
        souvenir_price = 4.20
    elif souvenir_type == "caps":
        souvenir_price = 8.50
    elif souvenir_type == "posters":
        souvenir_price = 5.35
    elif souvenir_type == "stickers":
        souvenir_price = 1.20
    else:
        print("Invalid stock!")
        invalid = True

elif football_team == "Croatia":
    if souvenir_type == "flags":
        souvenir_price = 2.75
    elif souvenir_type == "caps":
        souvenir_price = 6.90
    elif souvenir_type == "posters":
        souvenir_price = 4.95
    elif souvenir_type == "stickers":
        souvenir_price = 1.10
    else:
        print("Invalid stock!")
        invalid = True

elif football_team == "Denmark":
    if souvenir_type == "flags":
        souvenir_price = 3.10
    elif souvenir_type == "caps":
        souvenir_price = 6.50
    elif souvenir_type == "posters":
        souvenir_price = 4.80
    elif souvenir_type == "stickers":
        souvenir_price = 0.90
    else:
        print("Invalid stock!")
        invalid = True
else:
    print("Invalid country!")
    invalid = True

total_souvenir_price = souvenir_price * souvenirs_count
if not invalid:
    print(f'Pepi bought {souvenirs_count} {souvenir_type} of {football_team} for {total_souvenir_price:.2f} lv.')






