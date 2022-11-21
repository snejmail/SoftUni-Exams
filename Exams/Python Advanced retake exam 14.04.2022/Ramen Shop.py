from collections import deque

ramen_bowls = [int(r) for r in input().split(', ')]
customers = deque([int(c) for c in input().split(', ')])

while customers and ramen_bowls:
    current_bowl = ramen_bowls[-1]
    current_customer = customers[0]

    if current_bowl == current_customer:
        ramen_bowls.pop()
        customers.popleft()
    elif current_bowl > current_customer:
        ramen_bowls[-1] -= current_customer
        customers.popleft()
    elif current_customer > current_bowl:
        customers[0] -= current_bowl
        ramen_bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls)}")
if customers and not ramen_bowls:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(y) for y in customers)}")

