adults = 0
kids = 0
money_for_toys = 0
money_for_sweaters = 0
command = input()

while command != "Christmas":
    age = int(command)

    if age <= 16:
        kids += 1
        money_for_toys += 5
    elif age > 16:
        adults += 1
        money_for_sweaters += 15

    command = input()

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")

