distributors = {}
clients = {}
command = input()
total_money_spent = 0.0
total_money_earned = 0.0

while command != "End":
    split_command = command.split()
    action = split_command[0]
    name = split_command[1]

    if action == "Deliver":
        money_spent = float(split_command[2])
        if name in distributors:
            distributors[name]['money_spent'] += money_spent
        else:
            distributors[name] = {'money_spent': money_spent}
        total_money_spent += money_spent

    elif action == "Return":
        money_returned = float(split_command[2])
        if name in distributors and money_returned <= distributors[name]['money_spent']:
            distributors[name]['money_spent'] -= money_returned
            if distributors[name]['money_spent'] <= 0:
                del distributors[name]

    elif action == "Sell":
        money_earned = float(split_command[2])
        if name in clients:
            clients[name]['money_earned'] += money_earned
        else:
            clients[name] = {'money_earned': money_earned}
        total_money_earned += money_earned

    command = input()

sorted_clients = sorted(clients.items(), key=lambda kvpt: (kvpt[0], kvpt[1]['money_earned']))
for client_name, money_spent_by_client in sorted_clients:
    print(f"{client_name}: {money_spent_by_client['money_earned']:.2f}")
print("-----------")
sorted_distributors = sorted(distributors.items(), key=lambda kvpt: (kvpt[0], kvpt[1]['money_spent']))
for distributor_name, ingredients_purchased_cost in sorted_distributors:
    print(f"{distributor_name}: {ingredients_purchased_cost['money_spent']:.2f}")
print("-----------")
print(f"Total Income: {total_money_earned:.2f}")


