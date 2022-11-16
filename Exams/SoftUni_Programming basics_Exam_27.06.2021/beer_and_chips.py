from math import ceil

fan_name = input()
budget = float(input())
beer_bottles_count = int(input())
chips_packets_count = int(input())

beer_bottle_price = 1.20
beers_total_price = beer_bottle_price * beer_bottles_count
chips_packet_price = beers_total_price * 0.45
chips_total_price = ceil(chips_packet_price * chips_packets_count)
total_price = beers_total_price + chips_total_price
diff = abs(round(budget-total_price, 2))

if total_price <= budget:
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{fan_name} needs {diff:.2f} more leva!")
